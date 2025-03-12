'''7. Agora coloque um range fixo de 0 até 1000, você ainda tem a mesma opinião quanto a simetria? [plt.hist(dado, bins=_, range=[0, 1000])'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")

coluna_redacao = "Redação"
coluna_linguagens = "Linguagens"

coluna_redacao in df.columns
plt.figure(figsize=(10, 6))
plt.hist(df[coluna_redacao].dropna(), bins=range(0, 1000 + 20, 20), range=[0, 1000], edgecolor='black')
plt.title("Histograma de Redação (Intervalo Fixo 0-1000)")
plt.xlabel("Notas")
plt.ylabel("Frequência")
plt.show()

coluna_linguagens in df.columns
plt.figure(figsize=(10, 6))
plt.hist(df[coluna_linguagens].dropna(), bins=range(0, 1000 + 20, 20), range=[0, 1000], edgecolor='black')
plt.title("Histograma de Linguagens (Intervalo Fixo 0-1000)")
plt.xlabel("Notas")
plt.ylabel("Frequência")
plt.show()