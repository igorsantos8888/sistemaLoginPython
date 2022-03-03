import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Cadastro

def RetornaSession():
    USUARIO = 'igor'
    SENHA = '26032007Igor'
    HOST = '127.0.0.1'
    BANCO = 'sistema_login'
    PORT = '3306'
    CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession()


class CadastroUser:
    @classmethod
    def cadastrarUsuario(cls, nome, email, senha):
        
        usuario = list(session.query(Cadastro).filter(Cadastro.email == email).all())
        
        
        
        if len(usuario) > 0:
            return 1
        else:
            try:
                senha = hashlib.sha256(senha.encode()).hexdigest()
                cadastro = Cadastro(nome=nome, email=email, senha=senha)
                print('Cadastro realizado com sucesso')
                session.add(cadastro)
                session.commit()
            except:
                return 2
            


class LoginController:
    @classmethod
    def loginUsuario(cls, email, senha):
        
        senha = hashlib.sha256(senha.encode()).hexdigest()
        
        usuario = list(session.query(Cadastro).filter(Cadastro.email == email).filter(Cadastro.senha == senha).all())
        
        if len(usuario) > 0:
            if email == email and senha == senha:
                return 3
        else:
            return 4
                

        