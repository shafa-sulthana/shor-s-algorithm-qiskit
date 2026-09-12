import numpy as np

# Qubit |0>
zero = np.array([1, 0])

# Qubit |1>
one = np.array([0, 1])

# Pauli-X gate
X = np.array([
    [0, 1],
    [1, 0]
])

# Hadamard gate
H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

# Apply X gate to |0>
result_x = X @ zero

# Apply H gate to |0>
result_h = H @ zero

print("X|0> =", result_x)
print("H|0> =", result_h)
