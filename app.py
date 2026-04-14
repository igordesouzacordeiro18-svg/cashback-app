from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from cashback import calcular_cashback  # importa sua função
from db import salvar_consulta, buscar_historico

#Flask iniciado
app = Flask(__name__)
#Requisição entre frontend e backend
CORS(app)


@app.route('/')
def home():
    return render_template("index.html")


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

    #Captura IP do usuário
    ip = request.remote_addr

    #Define o tipo de cliente
    tipo_cliente = "VIP" if is_vip else "Normal"

    #Salva histórico da consulta
    salvar_consulta(ip, tipo_cliente, valor, resultado)

    return jsonify({"cashback": resultado, "status": "salvo no banco"})


# Rota principal (recebe dados frontend e retorna cashback)
@app.route('/cashback', methods=['POST'])
def cashback():
    try:
        data = request.json

        valor = float(data.get('valor') or 0)
        desconto = float(data.get('desconto') or 0)
        is_vip = str(data.get('vip')).lower() == "true"

        if valor <= 0:
            return jsonify({"error": "Valor inválido"}), 400

        resultado = calcular_cashback(valor, desconto, is_vip)

        if resultado is None:
            return jsonify({"error": "Erro no cálculo"}), 500

        ip = request.remote_addr
        tipo_cliente = "VIP" if is_vip else "Normal"

        try:
            salvar_consulta(ip, tipo_cliente, valor, resultado)
        except:
            pass
    
        return jsonify({
            "cashback": resultado,
            "status": "ok"
        })

    except Exception as e:
        print("ERRO BACKEND:", e)
        return jsonify({"error": "Erro interno"}), 500
    
#Retorna histórico de consultas do usuário baseado no IP
@app.route('/historico')
def historico():
    return jsonify([])


if __name__ == '__main__':
    app.run(debug=True)