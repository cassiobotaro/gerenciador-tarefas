from fastapi import FastAPI

app = FastAPI()
TAREFAS = []

@app.get("/tarefas")
def listar_tarefas():
    return TAREFAS