

# View - informação que o usuário irá solicitar.
def formulario_login():
    usuario_digitado = input("Informa o seu usuário: ")
    senha_digitado = input("informa a sua senha: ")
    usuario_completo = [usuario_digitado, senha_digitado]
    return usuario_completo

def exibir_mensagem(texto):
    print("\n\n")
    print("==========================")
    print(texto)
    print("==========================")
    print("\n\n")


