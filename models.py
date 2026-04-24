from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CifraMedica(Base):
    __tablename__ = "cifras_medicas"

    id = Column(Integer, primary_key=True, index=True)
    titulo_original = Column(String, index=True)
    doi_link = Column(String)
    is_premium = Column(Boolean, default=False) 
    hook_clinico = Column(String) 
    pico_populacao = Column(String)
    pico_intervencao = Column(String)
    pico_controle = Column(String)
    pico_desfecho = Column(String)
    tamanho_amostra = Column(String)
    nnt_impacto = Column(String) 
    bottom_line = Column(Text)
    analise_critica = Column(Text)
