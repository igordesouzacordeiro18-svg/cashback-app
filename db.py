dados_fake = []

def salvar_consulta(ip, tipo_cliente, valor, cashback):
    dados_fake.append((ip, tipo_cliente, valor, cashback))

def buscar_historico(ip):
    return [d[1:] for d in dados_fake if d[0] == ip][-10:]