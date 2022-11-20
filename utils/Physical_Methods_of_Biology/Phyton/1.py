import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 100
p = 0.5
size = 1000

def gaussian(x, m, s):
    return 1 / np.sqrt(2 * np.pi * s**2) * np.exp(-(x - m)**2 / (2 * s**2))

# random sample from binomial distribution
x = np.random.binomial(n, p, size)
# draw binomial distribution
x_values =np.arange(n+1)
y_values = [binom.pmf(x, n, p) for x in x_values] # creating a list of a number of values in which every value is a binomial calculated on the x_value list

# draw gaussian distribution
x_gauss = np.linspace(0, n+1, 1000)
y_gauss = gaussian(x_gauss, n*p, np.sqrt(n*p*(1-p)))

plt.figure()
plt.hist(x, density=True, color='yellow', edgecolor='black', rwidth=0.85)
plt.plot(x_values, y_values, color='red')
plt.plot(x_gauss, y_gauss, color='blue')
plt.show()