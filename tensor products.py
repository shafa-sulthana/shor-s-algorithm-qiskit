import numpy as np

# Single-qubit states
zero = np.array([1, 0])
one = np.array([0, 1])

# Tensor products
zero_zero = np.kron(zero, zero)
zero_one = np.kron(zero, one)
one_zero = np.kron(one, zero)
one_one = np.kron(one, one)

print("|00> =", zero_zero)
print("|01> =", zero_one)
print("|10> =", one_zero)
print("|11> =", one_one)
