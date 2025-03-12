# 1. Qual das disciplinas tem a maior amplitude de nota?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")

def calculo_amplitude(df):
    df1 = df.describe()
    df1.loc["amplitude"] = df1.loc['max'] - df1.loc['min']
    return df1
colunas_notas = ["Linguagens", "Ciências humanas", "Ciências da natureza", "Matemática", "Redação"]

amplitudes = {}
for coluna in colunas_notas:
    if coluna in df.columns:
        amplitudes[coluna] = calculo_amplitude(df[[coluna]]).loc["amplitude", coluna]
    else:
        print(f"A coluna '{coluna}' não foi encontrada no DataFrame.")

if amplitudes:
    maior_amplitude = max(amplitudes.values())
    disciplina_maior_amplitude = max(amplitudes, key=amplitudes.get)

    print(f"A disciplina com a maior amplitude de notas é '{disciplina_maior_amplitude}', com amplitude de {maior_amplitude}.")
