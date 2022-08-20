import pandas as pd

weather = pd.DataFrame({
    'city': ['oc','la','sf'],
    'temp': [32,45,30],
    'humidity': [80,60,78]
})

print(weather)


weather2 = pd.DataFrame({
    'city': ['ny', 'chicago', 'orlando'],
    'temp': [50, 5, 12],
    'humidity': [50, 90, 55]
})

print(weather2)

df = pd.concat([weather,weather2], keys=['west','east'])

print(df)
print(df.loc['east'])

temp_df = pd.DataFrame({
    'temp': [50, 5, 12],
    'city': ['ny', 'chicago', 'orlando']
})

wind_df = pd.DataFrame({
    'windspeed': [16, 50, 32],
    'city': ['ny', 'chicago', 'orlando']
})


df2 = pd.concat([temp_df, wind_df], axis=1)
print(df2)

temp_df2 = pd.DataFrame({
    'temp': [50, 5],
    'city': ['chicago', 'ny']
}, index=[0,1,])

wind_df2 = pd.DataFrame({
    'windspeed': [16, 50, 32],
    'city': ['ny', 'chicago', 'orlando']
}, index=[1, 0, 2])
# create indexes in order to concant with varying data
df3 = pd.concat([temp_df2, wind_df2], axis=1)
print(df3)
