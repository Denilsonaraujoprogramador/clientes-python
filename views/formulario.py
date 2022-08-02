

# View - informação que o usuário irá solicitar.
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("informe a sua senha: ")
    usuario_completo = [usuario_digitado, senha_digitado]
    return usuario_completo

def exibir_mensagem(texto):
    print("\n\n")
    print("==========================")
    print(texto)
    print("==========================")
    print("\n\n")

def menu():
    print(" 1 - Para cadastrar novo cliente")
    print(" 2 - Para listar todos os cliente")
    print(" 3 - Para sair")
    opcao = input("Digite a opção")
    return opcao

def cadastro_cliente():
    nome = input("Informe o nome: ")
    telefone = input("Informe o telefone: ")
    cliente=[nome,telefone]
    return cliente