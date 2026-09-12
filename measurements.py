from qiskit import QuantumCircuit

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Create superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Display the circuit
print(qc.draw())
