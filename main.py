from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy import create_engine
from models import Base, CifraMedica

# 1. Conexão com o Banco de Dados
engine = create_engine("sqlite:///synapse.db")
Base.metadata.create_all(engine)

app = FastAPI(title="API Synapse")

# 2. Configurando o Painel Admin (Sem hacks, apenas o código oficial)
admin = Admin(app, engine)

# 3. Criando a Tela de Gestão
class CifraMedicaAdmin(ModelView, model=CifraMedica):
    column_list = [CifraMedica.id, CifraMedica.titulo_original, CifraMedica.is_premium]
    name = "Cifra Médica"
    name_plural = "Cifras Médicas"

admin.add_view(CifraMedicaAdmin)

@app.get("/")
def home():
    return {"status": "Motor do Synapse Rodando Perfeitamente"}
