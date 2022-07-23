import controllers.validacao as validacao


# View - informação que o usuário irá solicitar.
def formulario_login():
    usuario_digitado = input("Informa o seu usuário: ")
    senha_digitado = input("informa a sua senha: ")
    validacao.validar_login(usuario_digitado, senha_digitado)
