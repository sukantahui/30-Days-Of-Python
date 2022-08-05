import numpy as np


x = np.arange(15, dtype=np.int64).reshape(3, 5)
print(x)
x[1:, ::2] = -99
print(x)

k=x.max(axis=0)
print(k)

rng = np.random.default_rng(12345)

print(rng)