'''9. Remova todos os outliers e verifique se eles são passíveis de alterar a média nacional significativamente? (considere significativamente um valor
acima de 5%)'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")
coluna_cienciasnatureza = "Ciências da natureza"
coluna_redacao = "Redação"

colunas_notas = [coluna_cienciasnatureza, coluna_redacao] 

# Remover outliers e calcular médias
for coluna in colunas_notas:
    if coluna in df.columns:
        Q1 = df[coluna].quantile(0.25)
        Q3 = df[coluna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

# Remover outliers
df_sem_outliers = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]

# Calcular médias
media_original = df[coluna].mean()
media_sem_outliers = df_sem_outliers[coluna].mean()

# Calcular diferença percentual
diferenca_percentual = abs((media_sem_outliers - media_original) / media_original) * 100

# Verificar se a diferença é significativa
if diferenca_percentual > 5:
    print(f"A remoção de outliers em {coluna} alterou a média nacional significativamente ({diferenca_percentual:.2f}%).")
else:
    print(f"A remoção de outliers em {coluna} não alterou a média nacional significativamente ({diferenca_percentual:.2f}%).")