from qiskit import QuantumCircuit

# Create 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Create superposition
qc.h(0)

# Entangle the qubits
qc.cx(0, 1)

# Measure both qubits
qc.measure(0, 0)
qc.measure(1, 1)

# Display the circuit
print(qc.draw())
