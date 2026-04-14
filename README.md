💰 CASHBACK APP - FINTECH CHALLENGE

Aplicação desenvolvida como parte de um desafio técnico para vaga de estágio em uma fintech.
O sistema calcula cashback com base em regras de negócio e registra histórico de consultas por IP.

Acesse o projeto online

👉 https://cashback-app-1.onrender.com

REGRAS DO NEGÓCIO

O cálculo do cashback segue as regras abaixo:

Cashback base: 5% sobre o valor final da compra (após desconto)
Clientes VIP recebem +10% de bônus sobre o cashback base
Compras acima de R$ 500 recebem o cashback dobrado (para todos os clientes)

⚙️ TECNOLOGIAS UTILIZADAS
Python (Flask)
HTML5
CSS3
JavaScript (Vanilla JS)
MySQL
Gunicorn
Render (deploy)

FUNCIONALIDADES
-Cálculo de cashback em tempo real
-Identificação de cliente VIP
-Aplicação de regras de negócio dinâmicas
-Histórico de consultas por IP
-API REST com Flask
-Frontend integrado via fetch API


ESTRUTURA DO PROJETO
Cashback-app/
│
├── app.py                # Backend Flask (API)
├── db.py                 # Conexão e queries do banco
├── cashback.py          # Lógica de cálculo de cashback
├── requirements.txt     # Dependências do projeto
│
├── templates/
│   └── index.html       # Frontend principal
│
├── static/
│   └── style.css        # Estilização do site
│
└── README.md
