import numpy as np
import pickle

mil_primes = np.load("./tools/data/primes_lt_1mil.npy")
bil_primes = np.load("./tools/data/primes_smaller_2bil.npy")

with open("./tools/data/1mil.pickle", "rb") as pf:
    mil_primes_dict = pickle.load(pf)