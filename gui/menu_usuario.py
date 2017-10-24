﻿from logica import usuario

def menu_adicionar():
    print ("\nAdicionar Usuario \n")
    cpf = int(input("CPF: "))
    nome = str(input("Nome: "))
    email = input("Email: ")
    senha = input("Senha: ")
    usuario.adicionar_usuario(cpf, nome, email, senha)

def imprimir_usuario(usuario):
    print ("CPF: ",  usuario[0])
    print ("Nome: ", usuario[1])
    print ("Email: ",  usuario[2])
    print ("Senha: ",  usuario[3])
    print ()

def menu_listar():
    print ("\nListar Usuarios \n")
    usuarios = usuario.listar_usuarios()
    for user in usuarios:
        imprimir_usuario(user)

def menu_buscar():
    print ("\nBuscar Usuario por CPF \n")
    cpf = int(input("CPF: "))
    user = usuario.buscar_usuario(cpf)
    if (user == None):
        print ("Usuario não encontrado.")
    else:
        imprimir_usuario(user)
  
def menu_remover():
    print ("\nRemover Usuario \n")
    cpf = int(input("CPF: "))
    user = usuario.remover_usuario(cpf)
    if (user == False):
        print ("Usuario não encontrado.")
    else:
        print ("Usuario removido.")
    

def mostrar_menu():
    run_usuario = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Usuario \n" +
             "(2) Listar Usuario \n" +
             "(3) Buscar Usuario por CPF \n" +
             "(4) Remover Usuario \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_usuario):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif (op == 4):
            menu_remover()
        elif (op == 0):
            run_usuario = False
    
