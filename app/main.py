from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import time_controller
from database.config import create_database

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar para permitir domínios específicos se necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(time_controller.router)


@app.on_event("startup")
async def startup_event():
    create_database()  # Chama a função para criar o banco de dados, se necessário


@app.get("/")
def read_root():
    return {"message": "Welcome to the Time Entry API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
