import numpy as np
import matplotlib.pyplot as plt

n = 600
die = [1,2,3,4,5,6]
res = [0] * len(die) # create a list of zeros of the lenght of die

pro_fair = [1/6] * len(die)
pro_unfair = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

plt.figure()
plt.hlines(n/6, xmin=0, xmax=7, color='red' ,linestyles='dashed')
for i in range(n):
    r = np.random.choice(die p=pro_fair)
    res[r - 1] += 1
    plt.bar(die, res)
    plt.xlim(0, 7)
    plt.ylim(0, n/2)
    plt.pause(0.05)