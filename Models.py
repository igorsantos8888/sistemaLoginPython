
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = 'igor'
SENHA = '26032007Igor'
HOST = '127.0.0.1'
BANCO = 'sistema_login'
PORT = '3306'
CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Cadastro(Base):
    __tablename__ = 'cadastro'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(50), nullable=True)
    email = Column(String(30), nullable=True)
    senha = Column(String(30), nullable=True)
    
Base.metadata.create_all(engine)