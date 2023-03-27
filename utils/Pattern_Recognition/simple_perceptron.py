import numpy as np

# Let's try to implement a simple perceptron (AND function)

if __name__ == "__main__":
    n_inputs = 2

    # initialize random weights
    weights = np.random.uniform(low=0, high=1, size=n_inputs)
    # my input
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # my target
    t = np.array([[0], [0], [0], [1]])
    # learning rate
    gamma = .01
    for epoch in range(10000):
        n_errors = 0
        for xi, ti in zip(x, t):
            y = np.sum(weights * xi) > 0
            error = ti - y
            weights += gamma * error * xi
            n_errors += error
        
        if n_errors == 0:
            break

    print(weights)
