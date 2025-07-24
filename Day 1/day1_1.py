# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 12:24:18 2025

@author: Asus
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/iakidesantos/Advent-of-code-2024/refs/heads/main/Day%201/day1_input.txt'
df = pd.read_csv(url, sep='\s+', header=None)
df_sorted = df.apply(sorted)
df_sorted['diff'] = abs(df_sorted[1]-df_sorted[0])
result = sum(df_sorted['diff'])
print(result)