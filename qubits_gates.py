from qiskit import QuantumCircuit

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# X gate 
qc.x(0)

# Y gate
qc.y(0)

# Z gate
qc.z(0)

# H gate - creates superposition
qc.h(0)

# Display the circuit
print(qc.draw())
