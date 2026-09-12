from qiskit import QuantumCircuit
import numpy as np


def qft(n):
    """
    Create an n-qubit Quantum Fourier Transform circuit.
    """

    qc = QuantumCircuit(n, name="QFT")

    for j in range(n):
        qc.h(j)

        for k in range(j + 1, n):
            angle = np.pi / (2 ** (k - j))
            qc.cp(angle, k, j)

    # Reverse the qubit order
    for i in range(n // 2):
        qc.swap(i, n - i - 1)

    return qc


# Example: 3-qubit QFT
qc = qft(3)

print(qc.draw())
