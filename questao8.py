'''8. Faça um boxplot para as notas de Ciências da Natureza e Redação, analisando os quartis e identificando possíveis outliers. Utilize o método
IQR (Intervalo Interquartílico) para essa análise.'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")

coluna_cienciasnatureza = "Ciências da natureza"
coluna_redacao = "Redação"

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[[coluna_cienciasnatureza, coluna_redacao]])
plt.title("Boxplots de Ciências da Natureza e Redação")
plt.ylabel("Notas")
plt.show()

for coluna in [coluna_cienciasnatureza, coluna_redacao]:
    if coluna in df.columns:
        Q1 = df[coluna].quantile(0.25)
        Q3 = df[coluna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)][coluna]
        print(f"Outliers em {coluna}:")
        print(outliers)