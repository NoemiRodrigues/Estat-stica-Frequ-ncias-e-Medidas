'''4. Se todos esses estudantes aplicassem para ciência da computação e existem apenas 40 vagas, qual seria a variância e média da nota dos
estudantes que entraram no curso de ciência da computação? '''

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
pesos = {
    "Redação": 2,
    "Matemática": 4,
    "Linguagens": 2,
    "Ciências Humanas": 1,
    "Ciências da Natureza": 1
}
    
df["nota_ponderada"] = 0
for disciplina, coluna in colunas_notas.items():
    if coluna in df.columns:
        df["nota_ponderada"] += df[coluna] * pesos[disciplina]
        
df_ordenado = df.sort_values(by="nota_ponderada", ascending=False)

# Selecionar os 40 melhores estudantes
top_40 = df_ordenado.head(40)

# Calcular a média e a variância das notas ponderadas
media_ponderada = top_40["nota_ponderada"].mean()
variancia_ponderada = top_40["nota_ponderada"].var()

# Imprimir os resultados
print(f"Média ponderada dos 40 melhores estudantes: {media_ponderada:.2f}")
print(f"Variância ponderada dos 40 melhores estudantes: {variancia_ponderada:.2f}")