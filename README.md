# Analisador de Sentimentos - E-commerce

Este projeto utiliza Processamento de Linguagem Natural (PLN) para analisar o sentimento de feedbacks de clientes em uma operação de e-commerce. O objetivo é automatizar a classificação de avaliações para identificar rapidamente clientes satisfeitos e oportunidades de melhoria.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal.
- **Pandas**: Manipulação e estruturação dos dados.
- **TextBlob**: Biblioteca de IA para análise de sentimentos.
- **UV**: Gerenciamento de ambiente virtual e pacotes.

## Estrutura do Projeto

- `data/`: Contém os arquivos CSV de entrada e o resultado gerado.
- `src/`: Scripts Python com a lógica de análise.
- `requirements.txt`: Lista de dependências do projeto.
- `.venv/`: Ambiente virtual isolado.

# E-commerce AI: Aspect-Based Sentiment Analysis (ABSA)

<div align="center">
  <img src="https://img.shields.io/badge/Python-Data_Engineering-%23704214?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Hugging_Face-NLP-%23FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-%23FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
</div>

---

## Objetivo de Negócio

No setor de e-commerce, uma simples avaliação de "3 estrelas" não diz à gestão onde está o problema. O cliente odiou o produto ou a entrega atrasou?

Para resolver essa dor, construí uma aplicação de **Inteligência Artificial de nível empresarial** utilizando Processamento de Linguagem Natural (NLP). O sistema lê os comentários dos clientes, divide o texto e avalia o sentimento (Positivo, Neutro ou Negativo) isoladamente para cada departamento: **Produto, Logística e Atendimento**.

## Arquitetura e Solução Técnica

A solução atua como um pipeline de dados analítico:

1. **Motor de Inferência (Hugging Face):** Utilização do modelo Transformer `nlptown/bert-base-multilingual-uncased-sentiment` para classificar o sentimento com precisão em português.
2. **Lógica de Negócio (Python):** Algoritmo personalizado de fragmentação de texto, mapeando palavras-chave para departamentos específicos, evitando viés cruzado (ex: elogio ao tecido, mas crítica à entrega).
3. **Data App (Streamlit & Plotly):** Interface web interativa permitindo testes unitários e processamento em lote (upload de CSV) com visualização gráfica instantânea dos gargalos da operação.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Machine Learning / NLP:** `transformers`, `torch`
- **Manipulação de Dados:** `pandas`
- **Front-end & BI:** `streamlit`, `plotly`

---

## Valor para o Cliente

Como **Engenheira de Dados**, desenvolvi este projeto para demonstrar como a extração inteligente de dados não estruturados (textos) pode otimizar estoques, reduzir custos de logística reversa e guiar decisões estratégicas em tempo real. **Disponível para adaptar este motor de NLP para analisar o banco de dados da sua empresa.**

## Como Executar o Projeto

1. **Clone o repositório:**
   ```bash

   ```

git clone [https://github.com/camilalarissa/sentiment-analysis-ecommerce.git](https://github.com/camilalarissa/sentiment-analysis-ecommerce.git)
