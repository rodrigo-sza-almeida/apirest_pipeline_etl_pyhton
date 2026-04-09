# 📊 Base de Dados (Dataset CSV)

Este diretório contém o arquivo de dados utilizado como ponto de partida para a pipeline de **ETL (Extract, Transform, Load)** do projeto. O arquivo fornece as informações brutas que serão processadas e enriquecidas através de Inteligência Artificial.

## 📄 O Arquivo: `dados.csv` (ou o nome do seu arquivo)

O arquivo `.csv` simula uma extração de um sistema legado ou banco de dados, contendo informações básicas dos usuários que desejamos engajar com mensagens personalizadas.

### 📋 Dicionário de Dados

| Coluna | Tipo | Descrição |
| :--- | :--- | :--- |
| `UserID` | Integer | Identificador único do usuário (Chave Primária). |
| `Nome` | String | Nome completo do usuário. |
| `Cargo` | String | Profissão ou cargo do usuário (utilizado para contextualizar o prompt da IA). |
| `Interesse` | String | Área de interesse para personalização do conteúdo. |
| `Mensagem_IA` | String | Coluna inicialmente vazia, a ser populada após o processamento do LLM. |

## ⚙️ Papel no Fluxo ETL

Este arquivo é a peça central da etapa de **Extraction (Extração)**:

1.  **Extração:** O script executado no Google Colab realiza a leitura deste arquivo `.csv` utilizando a biblioteca **Pandas**.
2.  **Transformação:** Para cada linha (usuário), os dados são enviados ao modelo de **IA Generativa**, que gera um texto personalizado com base nas colunas de interesse/cargo.
3.  **Carga:** Os dados transformados (enriquecidos) são então enviados via requisição `PUT` para a nossa **API REST** para atualizar o banco de dados final.

## 🛠️ Ferramentas de Manipulação
*   **Pandas:** Utilizado para leitura, filtragem e manipulação do DataFrame.
*   **Google Colab:** Ambiente onde o arquivo é carregado para processamento em nuvem.

---
