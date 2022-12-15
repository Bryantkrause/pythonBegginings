import numpy
import matplotlib.pyplot as plt

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)

print(x)

y = numpy.median(speed)

print(y)

z = numpy.std(speed)

print(z)

a = numpy.var(speed)

print(a)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

b = numpy.percentile(ages, 90)

print(b)

xx = numpy.random.normal(5.0, 1.0, 100000)

xaa = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
yaa = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(xaa, yaa)
plt.show()


