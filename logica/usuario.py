usuarios = []

def adicionar_usuario(cpf, nome, email, senha):    
    usuario = [cpf, nome, email, senha]
    usuarios.append(usuario)
    
def listar_usuarios():
    return usuarios

def buscar_usuario(cpf):
    for user in usuarios:
        if (user[0] == cpf):
            return user
    return None

def remover_usuario(cpf):
    for user in usuarios:
        if (user[0] == cpf):
            usuarios.remove(user)
            return True
    return False
        
def iniciar_usuarios():
    adicionar_usuario(36536539212, "GUSTAVO", "guh008@hotmail.com","teste123")
    adicionar_usuario(37538537212, "ALINE", "aline@hotmail.com","teste123")
