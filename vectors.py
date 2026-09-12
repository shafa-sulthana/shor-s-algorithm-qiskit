import numpy as np

# Qubit |0>
zero = np.array([1, 0])

# Qubit |1>
one = np.array([0, 1])

print("|0> =", zero)
print("|1> =", one)

# Equal superposition state
plus = (zero + one) / np.sqrt(2)

print("|+> =", plus)

# Probability of measuring 0 and 1
prob_0 = abs(plus[0]) ** 2
prob_1 = abs(plus[1]) ** 2

print("Probability of 0:", prob_0)
print("Probability of 1:", prob_1)
