from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TarefaDB(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    concluida = Column(Boolean, default=False)