from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

from shor_algorithm.qft import qft
from shor_algorithm.modular_exponentiation import (
    add_controlled_modular_exponentiation
)


def period_finding_circuit(N=15, a=2):
    """
    Quantum period-finding circuit for Shor's algorithm.
    """

    n_count = 4
    n_work = 4

    qc = QuantumCircuit(n_count + n_work, n_count)

    counting_qubits = list(range(n_count))
    work_qubits = list(range(n_count, n_count + n_work))

    # 1. Create superposition in counting register
    for qubit in counting_qubits:
        qc.h(qubit)

    # 2. Prepare work register in |1>
    qc.x(work_qubits[0])

    qc.barrier()

    # 3. Controlled modular exponentiation
    add_controlled_modular_exponentiation(
        qc,
        counting_qubits,
        work_qubits,
        a,
        N
    )

    qc.barrier()

    # 4. Apply inverse QFT
    inverse_qft = qft(n_count).inverse()

    qc.compose(
        inverse_qft,
        qubits=counting_qubits,
        inplace=True
    )

    qc.barrier()

    # 5. Measure counting register
    qc.measure(
        counting_qubits,
        range(n_count)
    )

    return qc


# ---------------------------------
# Run Shor period-finding example
# ---------------------------------

N = 15
a = 2

qc = period_finding_circuit(N, a)

print(qc.draw())


# Simulate
simulator = AerSimulator()

compiled_circuit = transpile(
    qc,
    simulator
)

result = simulator.run(
    compiled_circuit,
    shots=1024
).result()

counts = result.get_counts()

print("\nMeasurement results:")
print(counts)
