from qiskit import QuantumCircuit

# Create a circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to qubit 0
qc.h(0)

# Apply X gate to qubit 1
qc.x(1)

# Display the circuit
print(qc.draw())
