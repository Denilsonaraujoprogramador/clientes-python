

# Model - Infomação que virá da meu Banco de dados(BD) através de uma request do tipo GET(requisição).
def model_usuario():
    arquivo = open("models\\usuarios.txt","r+")
    bancodedados = arquivo.readlines()
    for usuario in bancodedados:
        usuario_senha = usuario.split(";")
    
    usuario_BD = usuario_senha[0]
    return usuario_BD

def model_senha():
    arquivo = open("models\\usuarios.txt","r+")
    bancodedados = arquivo.readlines()
    for usuario in bancodedados:
        usuario_senha = usuario.split(";")
    
    senha_BD = usuario_senha[1]
    return senha_BD

def model_cadastro_cliente(cliente):
    print("Cadastrado com Sucesso!")
