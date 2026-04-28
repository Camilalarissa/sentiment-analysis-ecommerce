import pandas as pd
from textblob import TextBlob

def analisar_sentimento(texto):
    
    analise = TextBlob(texto)
    
    
    if analise.sentiment.polarity > 0:
        return 'Positivo'
   
    elif analise.sentiment.polarity == 0:
        return 'Neutro'
   
    else:
        return 'Negativo'


df = pd.read_csv('data/feedbacks.csv')


df['sentimento'] = df['comentário'].apply(analisar_sentimento)

print(df)


df.to_csv('data/resultado_analise.csv', index=False)
