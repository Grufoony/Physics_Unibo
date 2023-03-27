import numpy as np
import time

def bad_implementation():
    print("Bad implementation")
    N = 100_000 # number of MC events
    N_run = 100 # number of runs
    Nhits = 0.0 # number of points accepted
    pi = np.zeros(N_run) # values of pi

    start_time = time.time() # start clock 
    for I in range(N_run):
        Nhits = 0.0
        for i in range(N):
            x = np.random.rand()*2-1
            y = np.random.rand()*2-1
            res = x*x + y*y
            if res < 1:
                Nhits += 1.0
        pi[I] += 4. * Nhits/N

    run_time = time.time()

    print("pi with ", N, " steps for ", N_run, " runs is ", np.mean(pi), " in ", run_time-start_time, " sec")
    print("Precision computation : ", np.abs(np.mean(pi)-np.pi))

def good_implementation():
    print("Good implementation")
    N = 100_000 # number of MC events
    N_run = 100 # number of runs

    start_time = time.time()

    rand = np.random.rand(N, N_run, 2)
    occ = np.count_nonzero(np.sum(rand**2, axis=2) < 1, axis=0)
    pi = 4 * occ / N

    run_time = time.time()

    print("pi with ", N, " steps for ", N_run, " runs is ", np.mean(pi), " in ", run_time-start_time, " sec")
    print("Precision computation : ", np.abs(np.mean(pi)-np.pi))

def prof_implementation():
    print("Prof implementation")
    N = 100_000 # number of MC events
    N_run = 100 # number of runs

    start_time = time.time()

    pos = np.random.uniform(-1, 1, size=(2, N, N_run))
    count = np.sum(np.sum(pos**2, axis=0) < 1, axis=0)
    pi = 4 * count / N

    run_time = time.time()

    print("pi with ", N, " steps for ", N_run, " runs is ", np.mean(pi), " in ", run_time-start_time, " sec")
    print("Precision computation : ", np.abs(np.mean(pi)-np.pi))

if __name__ == "__main__":
    bad_implementation()
    good_implementation()
    prof_implementation()