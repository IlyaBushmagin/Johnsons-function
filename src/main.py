import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_csv('ecg.csv', index_col='t')
print(f)

a = []
n = len(f)
for k in range(n):
	l = 1.0 / (n - k)
	sum = 0.0
	for j in range(n - k):
		delta = abs(f['ecg'][j + k] - f['ecg'][j])
		sum = sum + delta
	a.append(l * sum)

plt.plot(f, linewidth = 0.5)
plt.plot(a, linewidth = 0.5)
plt.show()
