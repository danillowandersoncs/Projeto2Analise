filmes = []

def adicionar_filme(titulo, genero, ano):    
    filme = [titulo, genero, ano, len(filmes) + 1]
    filmes.append(filme)
    
def listar_filmes():
    return filmes

def buscar_filme(cod_filme):
    if(cod_filme >= 0 and cod_filme <= len(filmes)):
        for i in range(0,len(filmes)):
            if(i==(cod_filme-1)):
                return filmes[i]
        return None
    return None

def buscar_filme_por_genero(genero):
    buscas = []
    for filme in filmes:
        if (filme[1] == genero):
            busca = [filme[0], filme[1], filme[2], filme[3]]
            buscas.append(busca)
    return buscas

def remover_filme(cod_filme):
    if(cod_filme >= 0 and cod_filme <= len(filmes)):
        for i in range(0,len(filmes)):
            if(i==(cod_filme-1)):
                return filmes[i]
        return None
    return False
        
def iniciar_filme():
    adicionar_filme("velozes e furioso", "ação","2001")
    adicionar_filme("Harry Potter", "ficção","2003")
