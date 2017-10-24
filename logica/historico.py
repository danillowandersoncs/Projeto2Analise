historicos = []

def registrar_filme_assistido (cod_filme, cpf):    
    historico = [cod_filme, cpf]
    historico.append(historico)
    
def listar_filmes_assistidos():
    return historicos
	
def listar_filmes_assistidos_por_cpf(cpf):
    for historico in historicos:
        if (historico[1] == cpf):
            return historico
    return None
