# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 12:24:18 2025

@author: Asus
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/iakidesantos/Advent-of-code-2024/refs/heads/main/Day%201/day1_input.txt'
df = pd.read_csv(url, sep='\s+', header=None)

df['Similarity_score'] = 0*df[0]

for i in range(len(df)):
    df['Similarity_score'][i] = df[0][i]*sum(df[0][i] == df[1][j] for j in range(len(df)))
    
print(sum(df['Similarity_score']))