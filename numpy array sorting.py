import numpy as np
a = np.array([34, 5, 89, 23, 76])
print(np.sort(a))
def sorting(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
print(sorting(a))
