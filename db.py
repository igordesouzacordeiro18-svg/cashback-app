import mysql.connector

def conectar():
    """
    Cria conexão com o banco MySQL local ou hospedado.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cashback_db"
    )


def salvar_consulta(ip, tipo_cliente, valor, cashback):
    """
    Salva uma nova consulta no banco MySQL.
    """

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO consultas (ip, tipo_cliente, valor, cashback)
    VALUES (%s, %s, %s, %s)
    """

    valores = (ip, tipo_cliente, valor, cashback)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def buscar_historico(ip):
    """
    Busca últimas 10 consultas do usuário baseado no IP.
    """

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT tipo_cliente, valor, cashback
    FROM consultas
    WHERE ip = %s
    ORDER BY id DESC
    LIMIT 10
    """

    cursor.execute(sql, (ip,))
    dados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return dados