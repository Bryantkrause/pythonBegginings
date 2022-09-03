import pandas as pd
import numpy as np
from datetime import date
import datetime as dt

file = 'project_data.csv'

df = pd.read_csv(file)

print(df.head())

print(df.tail())

print(df.info())

print(df['marital_status'].unique())
df['marital_status'] = df['marital_status'].replace('Widow','Widowed')
print(df['marital_status'].unique())

print(df.shape)
