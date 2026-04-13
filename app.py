from flask import Flask, request, jsonify
from flask_cors import CORS
from cashback import calcular_cashback  # importa sua função
from db import salvar_consulta, buscar_historico

app = Flask(__name__)
CORS(app)


# Rota inicial (só pra testar se a API está funcionando)
@app.route('/')
def home():
    return "API funcionando 🚀"


# Rota de teste (usa valores fixos)
@app.route('/teste')
def teste():
    resultado = calcular_cashback(600, 0.2, True)
    return jsonify({"cashback": resultado})


@app.route('/testar_salvar')
def testar_salvar():
    valor = 600
    desconto = 0.2
    is_vip = True

    resultado = calcular_cashback(valor, desconto, is_vip)

    ip = request.remote_addr
    tipo_cliente = "VIP" if is_vip else "Normal"

    salvar_consulta(ip, tipo_cliente, valor, resultado)

    return jsonify({"cashback": resultado, "status": "salvo no banco"})

# Rota principal (recebe dados)
@app.route('/cashback', methods=['POST'])
def cashback():
    data = request.json

    valor = data.get('valor')
    desconto = data.get('desconto')
    is_vip = data.get('vip')

    resultado = calcular_cashback(valor, desconto, is_vip)

    #PEGAR IP DO USUÁRIO
    ip = request.remote_addr

    #DEFINIR TIPO DE CLIENTE
    tipo_cliente = "VIP" if is_vip else "Normal"

    #SALVAR NO BANCO
    salvar_consulta(ip, tipo_cliente, valor, resultado)

    #RESPOSTA
    return jsonify({"cashback": resultado})

@app.route('/historico')
def historico():
    ip = request.remote_addr

    dados = buscar_historico(ip)

    resultado = []

    for item in dados:
        resultado.append({
            "tipo_cliente": item[0],
            "valor": item[1],
            "cashback": item[2]
        })

    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)