from qiskit import QuantumCircuit

# Create a circuit with 2 qubits
qc = QuantumCircuit(2)

# Create superposition
qc.h(0)

# Entangle the two qubits
qc.cx(0, 1)

# Display the circuit
print(qc.draw())
