'''3. Considerando o curso de Ciência da Computação da UFPE, onde o peso cada uma das disciplinas ponderado:
a. Redação - 2
b. Matemática e suas Tecnologias - 4
c. Linguagens, Códigos e suas Tecnologias - 2
d. Ciências Humanas e suas Tecnologias - 1
e. Ciências da Natureza e suas Tecnologias - 1
Qual o desvio padrão e média das notas dos 500 estudantes mais bem
colocados considerando esses pesos?'''

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
    "Ciências Humanas": "Ciências Humanas",
    "Ciências da Natureza": "Ciências da Natureza"
}
# Pesos das disciplinas
pesos = {
    "Redação": 2,
    "Matemática": 4,
    "Linguagens": 2,
    "Ciências Humanas": 1,
    "Ciências da Natureza": 1
}

# Calcular a nota ponderada para cada estudante
df["nota_ponderada"] = 0
for disciplina, coluna in colunas_notas.items():
    if coluna in df.columns:
        df["nota_ponderada"] += df[coluna] * pesos[disciplina]


# Ordenar os estudantes pela nota ponderada
df_ordenado = df.sort_values(by="nota_ponderada", ascending=False)

# Selecionar os 500 melhores estudantes
top_500 = df_ordenado.head(500)

# Calcular a média e o desvio padrão das notas ponderadas
media_ponderada = top_500["nota_ponderada"].mean()
desvio_padrao_ponderado = top_500["nota_ponderada"].std()

# Imprimir os resultados
print(f"Média ponderada dos 500 melhores estudantes: {media_ponderada:.2f}")
print(f"Desvio padrão ponderado dos 500 melhores estudantes: {desvio_padrao_ponderado:.2f}")