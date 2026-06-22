import pandas as pd
from transformers import pipeline

print("Iniciando o Motor de IA... (Baixando o modelo na primeira execução)")
# Usamos um modelo multilingue que entende português perfeitamente
analisador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# 1. Dicionário de Aspectos (Regras de Negócio do E-commerce)
aspectos_keywords = {
    "Produto": ["tecido", "tamanho", "qualidade", "vestido", "blusa", "costura", "cor"],
    "Logística": ["entrega", "prazo", "caixa", "rastreio", "chegou", "demorou", "correios"],
    "Atendimento": ["suporte", "atendente", "devolução", "troca", "site", "atendimento"]
}

# 2. Dados brutos simulados 
avaliacoes = [
    "O tecido do vestido é maravilhoso, mas a entrega demorou semanas.",
    "Chegou rápido, caixa intacta, mas a cor é bem diferente da foto no site.",
    "Péssimo suporte para devolução, não respondem. A qualidade da blusa até que é boa.",
    "Tamanho perfeito e caimento lindo. Entrega antes do prazo!"
]

def identificar_aspectos_e_sentimento(texto):
    resultados = []
    
    # Dividimos o texto em frases menores usando vírgulas e pontos
    frases = texto.replace(".", ",").split(",")
    
    for frase in frases:
        frase = frase.strip().lower()
        if not frase:
            continue
            
        aspecto_encontrado = None
        # Procura a qual departamento esta frase pertence
        for aspecto, palavras in aspectos_keywords.items():
            if any(palavra in frase for palavra in palavras):
                aspecto_encontrado = aspecto
                break
                
        # Se achou um aspecto, passa a IA apenas nesse trecho
        if aspecto_encontrado:
            # O modelo retorna de 1 a 5 estrelas. Vamos converter para texto.
            resultado_ia = analisador(frase)[0]
            estrelas = int(resultado_ia['label'].split(" ")[0])
            
            if estrelas >= 4:
                sentimento = "🟢 Positivo"
            elif estrelas == 3:
                sentimento = "🟡 Neutro"
            else:
                sentimento = "🔴 Negativo"
                
            resultados.append({
                "Trecho Analisado": frase.capitalize(),
                "Departamento": aspecto_encontrado,
                "Sentimento": sentimento,
                "Estrelas": estrelas
            })
            
    return resultados

# 3. Processamento do Pipeline
print("\n Analisando os reviews dos clientes...\n")
dados_processados = []

for idx, review in enumerate(avaliacoes):
    analises = identificar_aspectos_e_sentimento(review)
    for analise in analises:
        dados_processados.append({
            "ID_Review": idx + 1,
            "Review_Completo": review,
            **analise
        })

# 4. Exibição Profissional
df_resultados = pd.DataFrame(dados_processados)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(df_resultados[["ID_Review", "Departamento", "Sentimento", "Trecho Analisado"]])
print("\n Análise ABSA concluída com sucesso!")