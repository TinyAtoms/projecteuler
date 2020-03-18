import numpy as np
n = 125


def gen_multiples(start, stop):
    n = np.arange(start, stop)
    multiples = np.array([n, n * 2, n * 3, n * 4, n * 5, n * 6])
    return multiples


def filter_conditions(myarr):
    ar1 = np.array([set(str(i)) for i in myarr[0]])
    ar2 = np.array([set(str(i)) for i in myarr[1]])
    f1 = ar1 == ar2
    if not np.sum(f1):
        return None
    ar3 = np.array([set(str(i)) for i in myarr[2]])
    f2 = (ar1 == ar3)
    f1 = np.logical_and(f1, f2)
    if not np.sum(f1):
        return None
    ar4 = np.array([set(str(i)) for i in myarr[3]])
    f2 = (ar1 == ar4)
    f1 = np.logical_and(f1, f2)
    if not np.sum(f1):
        return None
    ar5 = np.array([set(str(i)) for i in myarr[4]])
    f2 = (ar1 == ar5)
    f1 = np.logical_and(f1, f2)
    if not np.sum(f1):
        return None
    ar6 = np.array([set(str(i)) for i in myarr[5]])
    f2 = (ar1 == ar6)
    f1 = np.logical_and(f1, f2)
    if not np.sum(f1):
        return None
    return myarr[0][f1]

for i in range(0, 100000):
    result = filter_conditions(gen_multiples(i * 100, i * 100 + 100))
    if result:
        print(result)
        break
