'''10. Considerando valores nulos, tente encontrar qual seria a melhor medida
de tendência que pode substituir as notas nulas. Média, moda ou mediana?
Substitua o valor por todos os três e diga qual delas altera menos a média
geral e o desvio padrão.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")
colunas_notas = {
    "Redação": "Redação",
    "Matemática": "Matemática",
    "Linguagens": "Linguagens",
    "Ciências Humanas": "Ciências humanas",
    "Ciências da Natureza": "Ciências da natureza"
}

metricas_originais = {}
for disciplina, coluna in colunas_notas.items():
    metricas_originais[disciplina] = {
        "media": df[coluna].mean(), #media
        "desvio_padrao": df[coluna].std()
    }

# Função para substituir nulos e calcular métricas
def calcular_metricas_substituicao(df, coluna, valor_substituicao):
    df_substituido = df[coluna].fillna(valor_substituicao)
    return {
        "media": df_substituido.mean(),
        "desvio_padrao": df_substituido.std()
    }

# Substituir nulos e calcular métricas
resultados = {}
for disciplina, coluna in colunas_notas.items():
    resultados[disciplina] = {}
    media = df[coluna].mean()
    moda = df[coluna].mode()[0]
    mediana = df[coluna].median()

    resultados[disciplina]["media"] = calcular_metricas_substituicao(df, coluna, media)
    resultados[disciplina]["moda"] = calcular_metricas_substituicao(df, coluna, moda)
    resultados[disciplina]["mediana"] = calcular_metricas_substituicao(df, coluna, mediana)

# Comparar e analisar
for disciplina, coluna in colunas_notas.items():
    print(f"Disciplina: {disciplina}")
    print(f"  Métricas originais: Média={metricas_originais[disciplina]['media']:.2f}, Desvio padrão={metricas_originais[disciplina]['desvio_padrao']:.2f}")

    for substituicao, metricas in resultados[disciplina].items():
        print(f"  Substituição por {substituicao}: Média={metricas['media']:.2f}, Desvio padrão={metricas['desvio_padrao']:.2f}")

    print("-" * 30)