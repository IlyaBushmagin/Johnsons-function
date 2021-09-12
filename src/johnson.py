import matplotlib.pyplot as plt
import math

n = 50
x = []
for i in range(n):
	x.append(i * math.sin(i))

a = []
for k in range(n):
	l = 1.0 / (n - k)
	sum = 0.0
	for j in range(n - k):
		delta = abs(x[j + k] - x[j])
		sum = sum + delta
	a.append(l * sum)

plt.plot(x, linewidth = 0.5)
plt.plot(a, linewidth = 0.5)
plt.show()
