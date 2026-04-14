# 💰 CASHBACK APP - FINTECH CHALLENGE

Aplicação desenvolvida como parte de um **desafio técnico** para vaga de estágio em uma fintech. O sistema calcula cashback com base em regras de negócio específicas e registra o histórico de consultas por IP.

🚀 **[Acesse o projeto online aqui](https://cashback-app-1.onrender.com)**

---

## 📋 Regras do Negócio

O cálculo do cashback segue os critérios abaixo:

* **Cashback Base:** 5% sobre o valor final da compra (após descontos).
* **Bônus VIP:** Clientes VIP recebem **+10% de bônus** sobre o valor do cashback base.
* **Super Cashback:** Compras acima de **R$ 500** recebem o cashback **dobrado** (válido para todos os clientes).

---

## ✨ Funcionalidades

* ✅ Cálculo de cashback em tempo real.
* ✅ Identificação de cliente VIP.
* ✅ Aplicação de regras de negócio dinâmicas.
* ✅ Histórico de consultas por IP.
* ✅ API REST com Flask.
* ✅ Frontend integrado via Fetch API.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python (Flask)
* **Frontend:** HTML5, CSS3, JavaScript 
* **Banco de Dados:** MySQL
* **Servidor/Deploy:** Gunicorn & Render

---

## 📂 Estrutura do Projeto

```text
Cashback-app/
├── app.py              # Backend Flask (API)
├── db.py               # Conexão e queries do banco
├── cashback.py         # Lógica de cálculo de cashback
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação do projeto
├── templates/
│   └── index.html      # Frontend principal
└── static/
    └── style.css       # Estilização do site
