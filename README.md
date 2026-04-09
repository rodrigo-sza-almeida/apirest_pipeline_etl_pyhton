# 🚀 API REST com Python, ETL e Integração com LLM

Este projeto consiste no desenvolvimento de uma **API REST utilizando Python e Flask**, integrada a um **pipeline de automação ETL** executado em ambiente de nuvem (Google Colab), com uso de **LLM (Large Language Model)** para geração de textos personalizados a partir de dados estruturados.

O objetivo principal foi consolidar conhecimentos em **desenvolvimento backend**, **integração entre ambientes local e nuvem**, **automação de processos** e **uso prático de IA generativa**.

---

## 🧩 Visão Geral da Arquitetura

```text
[ CSV ]
   ↓
ETL Pipeline (Colab)
   ↓
Transformação de Dados
   ↓
LLM (Geração de Texto)
   ↓
Banco de Dados
   ↓
API REST (Flask)
   ↓
Postman / Cliente
```

## ⚙️ Funcionalidades

✅ API REST para consumo de dados de usuários

✅ Pipeline ETL (Extract, Transform, Load)

✅ Leitura de dados a partir de arquivos CSV

✅ Integração com LLM para geração de texto personalizado

✅ Comunicação entre ambiente local e nuvem

✅ Testes de endpoints utilizando Postman


## 🛠️ Tecnologias Utilizadas

- Python
- Flask
- API REST
- Postman
- Google Colab
- ETL (Extract, Transform and Load)
- LLM (Large Language Model)
- CSV
- Banco de Dados (ambiente de testes)


## ▶️ Executando o Projeto Localmente

1. Clone o repositório:

```text
git clone https://github.com/seu-usuario/api-rest-etl-llm.git
```

2. Crie um ambiente virtual:

```text
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```text
pip install -r requirements.txt
```

4. Execute a aplicação:

```text
python src/app.py
```

5. Acesse os endpoints via Postman:
   
```text
http://localhost:5000
```

 ## ☁️ Pipeline ETL no Google Colab

O pipeline de automação foi desenvolvido e executado no Google Colab.

## 📎 Notebook do Colab:

👉 https://colab.research.google.com/drive/1eDhHF-cSfTx1tW86ECjoSCfSiF7RuGwm#scrollTo=jZaNm675eNR7

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram explorados conceitos importantes como:

- Construção de APIs REST com Flask
- Uso de decorators em Python
- Integração entre ambientes local e nuvem
- Automação de processos com ETL
- Consumo de modelos de IA generativa (LLM)
- Tratamento de bibliotecas obsoletas
- Boas práticas de organização de projetos backendhttps://github.com/rodrigo-sza-almeida


## 🎓 Créditos

Projeto desenvolvido como parte do Bootcamp da DIO (Digital Innovation One).

## 👨‍💻 Autor

Rodrigo Almeida

📍 Santo André - SP

🔗 LinkedIn: https://www.linkedin.com/in/rodrigo-de-souza-almeida/

📂 GitHub: https://github.com/rodrigo-sza-almeida

