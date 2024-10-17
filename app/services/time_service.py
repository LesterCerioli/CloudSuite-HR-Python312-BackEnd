import logging
import datetime
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class TimeService:
    def __init__(self, time, session_factory):
        """
        Initialize TimeService with a Time model and a session factory.
        :param time: SQLAlchemy Time model.
        :param session_factory: Callable that returns a new session object (default: Session).
        """
        self.time_model = time
        self.session_factory = session_factory

    def _log_processing(self, start_time, status, duration_ms):
        """
        Log the processing status with timestamps and duration.
        :param start_time: The start time of the processing.
        :param status: Status of the processing ('success' or 'failure').
        :param duration_ms: Duration of the processing in milliseconds.
        """
        logging.info({
            "date": start_time.date(),
            "start_time": start_time,
            "end_time": datetime.datetime.now(),
            "duration_ms": duration_ms,
            "status": status
        })

    def execute_with_retry(self, target_date, retry_count=3):
        """
        Executes the processing function with retries in case of failure.
        :param target_date: Date to query Time entries.
        :param retry_count: Number of retries on failure.
        """
        for attempt in range(retry_count):
            try:
                return self._process_times_for_date(target_date)
            except SQLAlchemyError as e:
                logging.error(f"Attempt {attempt + 1}/{retry_count} failed with error: {str(e)}")
                if attempt == retry_count - 1:
                    raise e

    def _process_times_for_date(self, target_date):
        """
        Processes Time entries for a specific date and logs the processing details.
        :param target_date: The date for which Time entries should be processed.
        """
        session = self.session_factory()
        try:
            start_time = datetime.datetime.now()

            # Querying the Time entries for the specific date
            time_entries = session.execute(
                select(self.time_model).where(self.time_model.date == target_date)
            ).scalars().all()

            if not time_entries:
                logging.info(f"No Time entries found for date: {target_date}")
                self._log_processing(start_time, status="success", duration_ms=0)
                return

            for entry in time_entries:
                logging.info(f"Processing Time entry: {entry.id} for date: {entry.date}")

            end_time = datetime.datetime.now()
            duration_ms = (end_time - start_time).total_seconds() * 1000
            self._log_processing(start_time, status="success", duration_ms=duration_ms)

        finally:
            session.close()

    def process_time_by_date(self, target_date: datetime.date):
        """
        Public method to process Time entries by date. It retries on failure.
        :param target_date: Date to query and process Time entries.
        """
        start_time = datetime.datetime.now()

        try:
            self.execute_with_retry(target_date)
        except SQLAlchemyError:
            end_time = datetime.datetime.now()
            duration_ms = (end_time - start_time).total_seconds() * 1000
            self._log_processing(start_time, status="failure", duration_ms=duration_ms)
            logging.error(f"Processing failed after all retries for date: {target_date}")
