from pydantic import BaseModel

class TarefaCreate(BaseModel):
    nome: str