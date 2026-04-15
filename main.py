from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base
import crud
import schemas

app = FastAPI()

# cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# 🔹 Criar tarefa
@app.post("/tarefas")
def criar(tarefa: schemas.TarefaCreate):
    db = SessionLocal()
    resultado = crud.criar_tarefa(db, tarefa)
    db.close()
    return resultado

# 🔹 Listar todas as tarefas
@app.get("/tarefas")
def listar():
    db = SessionLocal()
    resultado = crud.listar_tarefas(db)
    db.close()
    return resultado

# 🔹 Buscar tarefa por ID
@app.get("/tarefas/{id}")
def buscar(id: int):
    db = SessionLocal()
    tarefa = crud.buscar_tarefa(db, id)
    db.close()

    if tarefa:
        return tarefa
    return {"erro": "Tarefa não encontrada"}

# 🔹 Deletar tarefa
@app.delete("/tarefas/{id}")
def deletar(id: int):
    db = SessionLocal()
    sucesso = crud.deletar_tarefa(db, id)
    db.close()

    if sucesso:
        return {"mensagem": "Deletado"}
    return {"erro": "Não encontrado"}