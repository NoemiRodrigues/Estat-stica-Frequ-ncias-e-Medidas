'''6. Faça o histograma de Redação e Linguagens, de 20 em 20 pontos. Podemos dizer que são histogramas simétricos, justifique e classifique se
não assimétricas?'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")

coluna_redacao = "Redação"
coluna_linguagens = "Linguagens"

# Criar histograma de Redação
coluna_redacao in df.columns
plt.figure(figsize=(10, 6))
plt.hist(df[coluna_redacao].dropna(), bins=range(0, int(df[coluna_redacao].max()) + 20, 20), edgecolor='black')
plt.title("Histograma de Redação (Intervalos de 20 pontos)")
plt.xlabel("Notas")
plt.ylabel("Frequência")
plt.show()


# Criar histograma de Linguagens
coluna_linguagens in df.columns
plt.figure(figsize=(10, 6))
plt.hist(df[coluna_linguagens].dropna(), bins=range(0, int(df[coluna_linguagens].max()) + 20, 20), edgecolor='black')
plt.title("Histograma de Linguagens (Intervalos de 20 pontos)")
plt.xlabel("Notas")
plt.ylabel("Frequência")
plt.show()


print (" Como podemos perceber no histograma de Redação, temos uma cauda de ambos os lados e por isso ele é simétrico")
print (" Como podemos perceber no histograma de Linguagens, também temos uma cauda de ambos os lados e ele também é simétrico")