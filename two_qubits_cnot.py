from qiskit import QuantumCircuit

# Create a circuit with 2 qubits
qc = QuantumCircuit(2)

# Put qubit 0 into superposition
qc.h(0)

# Apply CNOT
qc.cx(0, 1)

# Display the circuit
print(qc.draw())
