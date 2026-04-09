# 📓 Automação de Processos: Pipeline ETL com IA Generativa

Este diretório contém o Jupyter Notebook (`.ipynb`) desenvolvido no **Google Colab**. Ele atua como o orquestrador da pipeline de dados, realizando a extração, a integração com modelos de linguagem de grande escala (LLMs) e a comunicação com a API local.

## 🚀 O Fluxo de Trabalho (ETL)

O notebook executa um processo completo de **Extract, Transform, and Load**:

1.  **Extract (Extração):** Leitura do arquivo `dados.csv` utilizando a biblioteca **Pandas**, mapeando os usuários que receberão as interações personalizadas.
2.  **Transform (Transformação):** 
    *   Consumo da API de um modelo de **IA Generativa** (ex: OpenAI GPT ou Google Gemini).
    *   Aplicação de **Prompt Engineering** para gerar textos personalizados com base nos dados extraídos (interesses, cargo, nome).
3.  **Load (Carga):** Envio dos dados enriquecidos para a **API REST** (desenvolvida em Flask) através de requisições HTTP, atualizando o banco de dados final.

## 🛠️ Tecnologias e Bibliotecas

*   **Python:** Linguagem base.
*   **Pandas:** Manipulação e análise de dados.
*   **Requests:** Para realizar as chamadas HTTP à nossa API REST.
*   **IA Generativa:** Integração com LLMs para geração de conteúdo dinâmico.
*   **Google Colab:** Ambiente de execução em nuvem.

## 🔗 Integração entre Nuvem e Local

Um dos destaques técnicos deste projeto foi o desafio de conectar o ambiente em nuvem do **Google Colab** com o servidor da **API local**. 
> **Nota:** Para que o Colab consiga "enxergar" a API rodando na sua máquina, foi utilizado um túnel de comunicação (como o **ngrok** ou localtunnel), garantindo que as requisições chegassem ao endpoint de destino.

## 📖 Como utilizar este Notebook

1.  Abra o arquivo no Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1eDhHF-cSfTx1tW86ECjoSCfSiF7RuGwm#scrollTo=jZaNm675eNR7)
2.  Certifique-se de que a API REST (pasta `/api`) esteja em execução.
3.  Configure sua **API KEY** da inteligência artificial nas variáveis de ambiente do notebook.
4.  Execute as células em ordem para processar o CSV e realizar a carga via API.

---
