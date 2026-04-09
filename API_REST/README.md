# 📂 API REST: Gerenciamento e Integração de Dados

Esta pasta contém o núcleo da API REST desenvolvida para o projeto de automação ETL. A API serve como ponte entre os dados armazenados e o script de processamento de IA (LLM) executado no Google Colab.

## 📄 Descrição dos Arquivos

### 🔹 `main.py`
É o ponto de entrada da aplicação. Desenvolvido utilizando o framework **Flask**, este arquivo:
*   Define as rotas (endpoints) da API.
*   Gerencia as requisições HTTP (GET, POST, PUT).
*   Utiliza **Decorators** para mapear as funções de resposta.
*   Realiza a lógica de integração com o serviço de IA para popular os dados processados.

### 🔹 `bd.py`
Este arquivo é responsável pela camada de persistência:
*   Contém a estrutura do banco de dados (ou simulador de banco de dados).
*   Implementa as funções de manipulação de dados (CRUD) que são chamadas pelo `main.py`.
*   Garante a organização dos dados dos usuários que serão consumidos pela pipeline ETL.

## 🛠️ Como Executar a API Localmente

1.  **Navegue até esta pasta:**
    ```bash
    cd nome-da-sua-pasta-api
    ```

2.  **Instale as dependências (Flask):**
    ```bash
    pip install flask
    ```

3.  **Inicie o servidor:**
    ```bash
    python main.py
    ```
    *A API iniciará por padrão no endereço `http://127.0.0.1:5000`*

## 🔌 Endpoints Principais

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| **GET** | `/users` | Lista todos os usuários registrados. |
| **GET** | `/users/<id>` | Busca um usuário específico por ID. |
| **PUT** | `/users/<id>` | Atualiza os dados do usuário (usado para inserir o texto gerado pela IA). |

## 💡 Observações Técnicas
Durante o desenvolvimento, foram aplicados conceitos de:
*   **Encapsulamento:** Separação da lógica de rotas (`main.py`) e lógica de dados (`bd.py`).
*   **Integração Local-Nuvem:** Configuração de acesso para que o ambiente do Google Colab pudesse realizar requisições para este servidor local (via ferramentas de tunelamento como ngrok, se aplicável).
