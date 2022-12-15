import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [1430992.8, 1458632.58, 1633701.11, 1552792.3, 1538099.45, 1666781.54, 1674055.1, 1727767.78, 1565967.23, 1376603.51, 1301282.808
     ]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 11, 100)

speed = mymodel(12)
print(speed)

print(r2_score(y, mymodel(x)))
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
