# 🚀 API de Tarefas com FastAPI

API REST desenvolvida com Python utilizando FastAPI para gerenciamento de tarefas.

---

## 📌 Funcionalidades

- Criar tarefas  
- Listar todas as tarefas  
- Buscar tarefa por ID  
- Deletar tarefas  

---

## 🛠️ Tecnologias utilizadas

- Python  
- FastAPI  
- SQLite  
- SQLAlchemy  

---

## 📂 Estrutura do projeto

fastapi-todo/
├── main.py        # Rotas da aplicação
├── crud.py        # Lógica do sistema
├── models.py      # Modelos do banco
├── schemas.py     # Validação de dados
├── database.py    # Conexão com banco
---

## ▶️ Como executar o projeto

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload