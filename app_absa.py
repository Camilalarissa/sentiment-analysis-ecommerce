import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import pipeline

# 1. Configuração da Página
st.set_page_config(page_title="AI E-commerce Analytics", page_icon="🛍️", layout="wide")

# 2. Carregar o Modelo de IA em Cache (Prática de Performance)
@st.cache_resource
def carregar_modelo():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

analisador = carregar_modelo()

# 3. Regras de Negócio (Dicionário de Aspectos)
aspectos_keywords = {
    "Produto": ["tecido", "tamanho", "qualidade", "vestido", "blusa", "costura", "cor"],
    "Logística": ["entrega", "prazo", "caixa", "rastreio", "chegou", "demorou", "correios"],
    "Atendimento": ["suporte", "atendente", "devolução", "troca", "site", "atendimento"]
}

# 4. Motor de Processamento
def analisar_texto(texto):
    resultados = []
    frases = texto.replace(".", ",").split(",")
    
    for frase in frases:
        frase = frase.strip().lower()
        if not frase: continue
            
        aspecto_encontrado = "Geral" # Fallback caso não ache palavra-chave
        for aspecto, palavras in aspectos_keywords.items():
            if any(palavra in frase for palavra in palavras):
                aspecto_encontrado = aspecto
                break
                
        resultado_ia = analisador(frase)[0]
        estrelas = int(resultado_ia['label'].split(" ")[0])
        
        if estrelas >= 4:
            sentimento = "Positivo"
        elif estrelas == 3:
            sentimento = "Neutro"
        else:
            sentimento = "Negativo"
            
        resultados.append({
            "Trecho": frase.capitalize(),
            "Departamento": aspecto_encontrado,
            "Sentimento": sentimento,
            "Estrelas": estrelas
        })
    return resultados

# 5. Interface Visual do Streamlit
st.title(" Radar de Sentimento Baseado em Aspectos (ABSA)")
st.markdown("Analise os comentários de clientes e descubra exatamente **o que** está a agradar e **onde** a operação está a falhar.")

# Criar duas abas: Uma para texto livre, outra para upload de arquivo
aba1, aba2 = st.tabs(["Teste Rápido (Texto)", " Análise em Massa (CSV)"])

with aba1:
    st.subheader("Cole o comentário do cliente:")
    texto_usuario = st.text_area("Exemplo: O tecido é ótimo, mas a entrega atrasou e o suporte não respondeu.", height=100)
    
    if st.button("Analisar Sentimento", type="primary"):
        if texto_usuario:
            with st.spinner("A inteligência artificial está a ler o comentário..."):
                dados = analisar_texto(texto_usuario)
                df = pd.DataFrame(dados)
                
                st.success("Análise Concluída!")
                st.dataframe(df, use_container_width=True)
                
                # Gráfico
                fig = px.bar(df, x="Departamento", y="Estrelas", color="Sentimento", 
                             color_discrete_map={"Positivo": "#28a745", "Neutro": "#ffc107", "Negativo": "#dc3545"},
                             title="Impacto por Departamento")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Por favor, digite um comentário.")

with aba2:
    st.subheader("Suba uma planilha de avaliações")
    st.markdown("O seu CSV deve conter uma coluna chamada **'comentario'**.")
    arquivo = st.file_uploader("Escolha um arquivo CSV", type=["csv"])
    
    if arquivo is not None:
        df_upload = pd.read_csv(arquivo)
        if 'comentario' in df_upload.columns:
            st.info(f"Analisando {len(df_upload)} comentários. Isso pode demorar alguns segundos...")
            
            resultados_massa = []
            for texto in df_upload['comentario'].dropna():
                resultados_massa.extend(analisar_texto(texto))
                
            df_final = pd.DataFrame(resultados_massa)
            
            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(df_final, use_container_width=True)
            with col2:
                # Gráfico de Pizza para ver os maiores problemas
                contagem = df_final.groupby(['Departamento', 'Sentimento']).size().reset_index(name='Quantidade')
                fig2 = px.sunburst(contagem, path=['Departamento', 'Sentimento'], values='Quantidade',
                                   color='Sentimento', color_discrete_map={"Positivo": "#28a745", "Neutro": "#ffc107", "Negativo": "#dc3545"},
                                   title="Visão Geral da Operação")
                st.plotly_chart(fig2, use_container_width=True)
        else:
            st.error("O arquivo precisa ter uma coluna com o título exato: 'comentario'")