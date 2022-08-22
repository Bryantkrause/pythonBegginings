import pandas as pd
import numpy as np

df = pd.DataFrame({'Type': list('ABBC'), 'Set': list('ZZXY')})
conditions = [
    (df['Set'] == 'Z') & (df['Type'] == 'A'),
    (df['Set'] == 'Z') & (df['Type'] == 'B'),
    (df['Type'] == 'B')]
choices = ['yellow', 'blue', 'purple']
df['color'] = np.select(conditions, choices, default='black')
print(df)

# https: // stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column
