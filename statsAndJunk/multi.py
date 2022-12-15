import pandas
from sklearn import linear_model

df = pandas.read_csv(r"C:\Users\bkrause\Documents\CodeMe\Rebirth\pythonBeginings\statsAndJunk\thingy.csv")

print(df.columns)
X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
regr = linear_model.LinearRegression()
regr.fit(X, y)
print(predictedCO2)
print(regr.coef_)
predictedCO22 = regr.predict([[3300, 1300]])

print(predictedCO22)
