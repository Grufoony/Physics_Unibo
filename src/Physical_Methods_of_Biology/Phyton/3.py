import numpy as np

n = 20000000
n_acc = 0

for i in range(n):
    x = np.random.random()
    y = np.random.random()

    if x**2 + y**2 <= 1:
        n_acc += 1

area = n_acc / n
pi = area * 4
error = np.abs(pi - np.pi) * 100

print("Estimated pi: %5.10f" % pi)
print("Error: %5.2f" % error)