import models.banco as banco
import views.formulario as view


# Controller - irá relalizar a validação a informação solicitada pelo usuário e oretorno do Banco de dados.
def validar_login(usuario_completo):
    usuario_BD = banco.model_usuario()
    senha_BD = banco.model_senha()
    if usuario_completo[0] == usuario_BD and usuario_completo[1] == senha_BD:
        view.exibir_mensagem("SC - Sistema de clientes")
        opcoes_menu()
    else:
        view.exibir_mensagem("Usuário ou senha inválidos")
        iniciar()

def iniciar():
    #validar_login(view.formulario_login())
    # essa seria uma forma menos didatica porem o mesmo cenario referente a linha acima.
    usuario_completo = view.formulario_login()
    validar_login(usuario_completo)

def opcoes_menu():
    opcao = view.menu()
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        print("Listagem de cliente")
    else:
        view.exibir_mensagem("Sistema finalizado")
        exit()

def cadastrar_cliente():
    cliente = view.cadastro_cliente()
    banco.model_cadastro_cliente(cliente)