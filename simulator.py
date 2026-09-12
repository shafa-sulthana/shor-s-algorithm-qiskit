from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit
qc = QuantumCircuit(1, 1)

# Put the qubit into superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Create simulator
simulator = AerSimulator()

# Run the circuit 1000 times
result = simulator.run(qc, shots=1000).result()

# Get measurement results
counts = result.get_counts()

print("Measurement results:")
print(counts)
