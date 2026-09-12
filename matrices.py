import numpy as np

# Pauli-X gate
X = np.array([
    [0, 1],
    [1, 0]
])

# Pauli-Y gate
Y = np.array([
    [0, -1j],
    [1j, 0]
])

# Pauli-Z gate
Z = np.array([
    [1, 0],
    [0, -1]
])

# Hadamard gate
H = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
])

print("X gate:")
print(X)

print("\nY gate:")
print(Y)

print("\nZ gate:")
print(Z)

print("\nHadamard gate:")
print(H)
