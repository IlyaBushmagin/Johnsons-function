import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_csv('ecg.csv', index_col = 't')
print(f)

n = len(f)
mu = f['ecg'].mean()
d = ((f['ecg'] - mu)**2).sum() / n

a = []
r = []
for k in range(n):
	l = 1.0 / ((n - k) * d)
	sum_a = 0.0
	sum_r = 0.0
	for j in range(n - k):
		sum_a = sum_a + abs(f['ecg'][j + k] - f['ecg'][j])
		sum_r = sum_r + (f['ecg'][j + k] - mu) * (f['ecg'][j] - mu)
	a.append(l * sum_a)
	r.append(l * sum_r)

plt.plot(f, linewidth = 0.5)
plt.show()
plt.plot(a, linewidth = 0.5)
plt.show()
plt.plot(r, linewidth = 0.5)
plt.show()
