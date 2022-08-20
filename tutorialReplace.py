import pandas as pd
import numpy as np

file = 'replace.xlsx'

df = pd.read_excel(file)

print(df)

ndf = df.replace([-99999,6, 'no event'],np.NaN)

rdf = df.replace({
    'temp': -99999,
    'wind': -99999,
    'event': 'no event'
}, 0)

print(rdf)

rdfr = df.replace({
    -99999: np.NAN,
    'no event': 'sunny'
})

print(rdfr)

dfNew = df.replace({
    'temp': '[A-Za-z]',
    'wind': '[A-Za-z]'
},'',regex=True)
print(dfNew)

more = pd.DataFrame({
    'score': ['exceptional', 'average', 'good', 'poor', 'average', 'exceptional'],
    'student':['rob','maya','parthiv', 'tom', 'julian','erica']
})

print(more)

newMore = more.replace(['poor', 'average', 'good', 'exceptional'],[1,2,3,4])
print(newMore)
