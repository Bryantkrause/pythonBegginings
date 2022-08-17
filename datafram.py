import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94, 60.665, 12.061, 64.511, 318.523],
    'GDP': [1785387, 2833687, 3874437, 2167744, 4602367, 295039, 17348075],
    'Surface Area': [9984670, 640679, 357114, 301336, 377930, 242495, 9525067],
    'HDI': [0.913, 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
    'Continent': ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America']
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

result = df.axes
chooser = str(input())
print(df.loc[df['Continent'] == chooser.capitalize(), 'Population'].sum())
print(63.951+80.94+60.665+64.511)



