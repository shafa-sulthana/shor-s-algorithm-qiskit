import numpy as np

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator


def modular_multiplication_matrix(a, N, n_work=4):
    """
    Create the unitary matrix for:

        |y> -> |a*y mod N>

    For states outside the modular range, the state is
    left unchanged.
    """

    dimension = 2 ** n_work
    matrix = np.zeros((dimension, dimension))

    for y in range(dimension):

        if y < N:
            result = (a * y) % N
        else:
            result = y

        matrix[result, y] = 1

    return matrix


def controlled_modular_power(
    qc,
    control_qubit,
    work_qubits,
    a,
    exponent,
    N
):
    """
    Apply controlled multiplication by:

        a^exponent mod N
    """

    n_work = len(work_qubits)

    multiplier = pow(a, exponent, N)

    matrix = modular_multiplication_matrix(
        multiplier,
        N,
        n_work
    )

    unitary = Operator(matrix).to_instruction()

    controlled_unitary = unitary.control(1)

    qc.append(
        controlled_unitary,
        [control_qubit] + list(work_qubits)
    )


def add_controlled_modular_exponentiation(
    qc,
    counting_qubits,
    work_qubits,
    a,
    N
):
    """
    Apply controlled U^(2^j) operations.
    """

    for j, control in enumerate(counting_qubits):

        exponent = 2 ** j

        controlled_modular_power(
            qc,
            control,
            work_qubits,
            a,
            exponent,
            N
        )


# Example
if __name__ == "__main__":

    N = 15
    a = 2

    n_count = 4
    n_work = 4

    qc = QuantumCircuit(n_count + n_work)

    counting_qubits = list(range(n_count))
    work_qubits = list(range(n_count, n_count + n_work))

    # Prepare work register in |1>
    qc.x(work_qubits[0])

    # Add controlled modular exponentiation
    add_controlled_modular_exponentiation(
        qc,
        counting_qubits,
        work_qubits,
        a,
        N
    )

    print(qc.draw())
