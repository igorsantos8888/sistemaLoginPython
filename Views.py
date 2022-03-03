import Controller

if __name__ == '__main__':
    while True:
        local = int(input('Digite 1 para acessar (Cadastrar)\n'
                          'Digite 2 para acessar (Login)\n'
                          'Digite 3 para sair do sistema\n'))
    
        if local == 1:
            cadastro = Controller.CadastroUser()
            while True:
                nome = input('Digite o seu nome: ')
                email = input('Digite o seu e-mail: ')
                senha = input('Digite a sua senha: ')
                cadUser = cadastro.cadastrarUsuario(nome, email, senha)
                
                if cadUser == 1:
                    print('Cadastro não foi realizado\n'
                          'E-mail já utilizado no sistema. Tente novamente.')
                elif cadUser == 2:
                    print('Erro interno do sistema')
                else:
                    print(cadUser)
                break
                
        if local == 2:
            login = Controller.LoginController()
            while True:
                email = input('Digite o seu email: ')
                senha = input('Digite sua senha: ')
                loginUser = login.loginUsuario(email, senha)
                
                if loginUser == 3:
                    print('Acesso autorizado. Bem vindo ao sistema!')
                else:
                    print('Acesso negado')
                    print('Senha ou email incorretos. tente novamente!')
                break
        else:
            break