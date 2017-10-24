from logica import filme

def menu_adicionar():
    print ("\nAdicionar Filme \n")
    titulo =input("Titulo: ")
    genero = input("Genero: ")
    ano = input("Ano: ")
    filme.adicionar_filme(titulo, genero, ano)

def imprimir_filme(_filme):
    print ("Titulo: ",_filme[0])
    print ("Genero: ",_filme[1])
    print ("Ano: ", _filme[2])
    print ("Cod_filme: ",_filme[3])
    print ()
	
def imprimir_filmes(filmes):
    for _filme in filmes:
        print("Titulo: ",_filme[0])
        print("Genero: ",_filme[1])
        print("Ano: ",_filme[2])
        print("Cod_filme: ",_filme[3])
        print()

def menu_listar():
    print ("\nListar Filmes \n")
    filmes = filme.listar_filmes()
    for _filme in filmes:
        imprimir_filme(_filme)

def menu_buscar():
    print ("\nBuscar Filme por Cod Filme \n")
    cod_filme = int(input("Cod_filme: "))
    _filme = filme.buscar_filme(cod_filme)
    if (_filme == None):
        print ("Filme não encontrado.")
    else:
        imprimir_filme(_filme)

def menu_buscar_por_genero():
    print ("\nBuscar Filme por genero \n")
    genero = input("Genero: ")
    _filmes = filme.buscar_filme_por_genero(genero)
    if (_filmes == None):
        print ("Filme não encontrado.")
    else:
        imprimir_filmes(_filmes)
  
def menu_remover():
    print ("\nRemover Filme \n")
    cod_filme = int(input("Cod_filme: "))
    _filme = filme.remover_filme(cod_filme)
    if (_filme == False):
        print ("Filme não encontrado.")
    else:
        print ("Filme removido.")
    
def mostrar_menu():
    run_filme = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Filme \n" +
             "(2) Listar Filme \n" +
             "(3) Buscar Filme por Cod_Filme \n" +
             "(4) Buscar Filme por Genero \n" +
             "(5) Remover Filme \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_filme):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            menu_adicionar()
        elif(op == 2):
            menu_listar()
        elif(op == 3):       
            menu_buscar()
        elif(op == 4):       
            menu_buscar_por_genero()
        elif(op == 5):
            menu_remover()
        elif(op == 0):
            run_filme = False
    
