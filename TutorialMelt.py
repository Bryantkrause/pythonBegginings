import pandas as pd


df = pd.DataFrame({
    'day': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
    'Chicago': [32,30,28,22,32,20,25],
    'Chennai': [75,77,75,82,83,81,77],
    'Berlin': [41,43,45,38,30,45,47]
})

print(pd.melt(df, id_vars=['day']))