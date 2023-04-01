import numpy as np
import matplotlib.pyplot as plt

nsteps = 10
nparticles = 1000

tm = [[1/2, 1/4, 1/4],
      [1/3, 0, 2/3],
      [1/2, 1/2, 0]]

solution = [0.457, 0.257, 0.286]

# one particle starting at state 0
# state = 0

# for nparticles

final_states = []
for j in range(nparticles):
    state = np.random.choice([0, 1, 2])
    for i in range(nsteps):
        p0 = tm[state][0]
        p1 = tm[state][1]
        p2 = tm[state][2]

        r = np.random.random()

        # see Arcelli
        if r < p0:
            state = 0
        elif r < p0 + p1:
            state = 1
        else:
            state = 2
    final_states.append(state)

plt.figure()
plt.hist(final_states, density=True)
plt.plot([0, 1, 2], solution, 'o')
plt.show()