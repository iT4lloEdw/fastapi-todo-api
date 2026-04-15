from models import TarefaDB

def criar_tarefa(db, tarefa):
    nova = TarefaDB(nome=tarefa.nome)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_tarefas(db):
    return db.query(TarefaDB).all()

def deletar_tarefa(db, id):
    tarefa = db.query(TarefaDB).filter(TarefaDB.id == id).first()
    if tarefa:
        db.delete(tarefa)
        db.commit()
        return True
    return False

# 👇 ADICIONE ISSO
def buscar_tarefa(db, id):
    return db.query(TarefaDB).filter(TarefaDB.id == id).first()