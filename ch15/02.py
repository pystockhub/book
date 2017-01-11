import matplotlib.pyplot as plt

x = range(0, 100)
y = [v*v for v in x]
plt.plot(x, y)
#plt.plot(x, y, 'ro')
plt.show()