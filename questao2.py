#Qual é a média e a mediana para cada uma das disciplinas? (Lembre-se de remover todos os valores nulos quando considerar a mediana)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")

colunas_notas = ["Linguagens", "Ciências humanas", "Ciências da natureza", "Matemática", "Redação"]

# Calcular a média e a mediana para cada disciplina
for coluna in colunas_notas:
    if coluna in df.columns:
        media = df[coluna].mean()
        mediana = df[coluna].dropna().median()  # Remove valores nulos antes de calcular a mediana
        print(f"Disciplina: {coluna}")
        print(f"  Média: {media:.2f}")
        print(f"  Mediana: {mediana:.2f}")