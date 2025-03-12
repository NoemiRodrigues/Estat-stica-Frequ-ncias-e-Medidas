'''5. Qual o valor do teto do terceiro quartil para as disciplinas de matemática
e linguagens?'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat

df = pd.read_json("enem_2023.json")
coluna_matematica = "Matemática"
coluna_linguagens = "Linguagens"

coluna_matematica in df.columns
q3_matematica = df[coluna_matematica].quantile(0.75)
print(f"Teto do terceiro quartil para Matemática: {q3_matematica:.2f}")

# Calcular o terceiro quartil para Linguagens
coluna_linguagens in df.columns
q3_linguagens = df[coluna_linguagens].quantile(0.75)
print(f"Teto do terceiro quartil para Linguagens: {q3_linguagens:.2f}")