import matplotlib.pyplot as plt
from scipy import stats

x = [1,2,3,4,5,6,7,8,9,10,11]
y = [1430992.8, 1458632.58, 1633701.11, 1552792.3, 1538099.45, 1666781.54, 1674055.1, 1727767.78, 1565967.23, 1376603.51, 1301282.808
     ]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
  return slope * x + intercept


mymodel = list(map(myfunc, x))


print(r)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

