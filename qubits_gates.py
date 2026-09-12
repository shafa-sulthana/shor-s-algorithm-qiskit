from qiskit import QuantumCircuit

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Apply Hadamard gate
qc.h(0)

# Display the circuit
print(qc.draw())
