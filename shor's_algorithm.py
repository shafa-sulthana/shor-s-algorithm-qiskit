!pip install -q qiskit qiskit-aer pylatexenc
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFTGate
import matplotlib.pyplot as plt
from math import gcd, log2, ceil
from fractions import Fraction
# ---------------------------------
# USER INPUT
# ---------------------------------
N = 15 # Number to factor
a = 2# Choose a such that gcd(a,N)=1
shots = 1024
# ---------------------------------
# CHECK VALIDITY OF a
# ---------------------------------
if gcd(a,N)!=1:
    print("Invalid a")
    print("Common factor found =", gcd(a, N))
else:
     print("Valid a =", a)
# ---------------------------------
# Number of counting qubits
# ---------------------------------
n_count = ceil(log2(N)) + 1
# Total qubits = counting + 1 target
qc = QuantumCircuit(n_count + 1, n_count)
# ---------------------------------
# Step 1: Superposition
# ---------------------------------
for q in range(n_count):
     qc.h(q)
# ---------------------------------
# Step 2: Target = |1>
# ---------------------------------
qc.x(n_count)
# ---------------------------------
# Step 3: Dynamic Phase Encoding
# ---------------------------------
for q in range(n_count):
     angle = (2 * 3.1416 * (a**(2**q) % N)) / N
     qc.cp(angle, q, n_count)
# ---------------------------------
# Step 4: Inverse QFT
# ---------------------------------
qc.append(QFTGate(n_count).inverse(), range(n_count))
# ---------------------------------
# Step 5: Measure
# ---------------------------------
qc.measure(range(n_count), range(n_count))
# ---------------------------------
# Draw Circuit
# ---------------------------------
#print(qc.draw('text'))
print(qc.draw(output='text', fold=-1))
# ---------------------------------
# Run Simulator
# ---------------------------------
sim = AerSimulator()
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=shots).result()
counts = result.get_counts()
print("Measurement Results:")
print(counts)
# Histogram
plot_histogram(counts)
plt.show()
# ---------------------------------
# Get Most Frequent State
# ---------------------------------
max_state = max(counts, key=counts.get)
decimal = int(max_state, 2)
phase = decimal / (2**n_count)
frac = Fraction(phase).limit_denominator(N)
r = frac.denominator
print("Estimated Period r =", r)
# ---------------------------------
#Try another a.")
# ---------------------------------
# Find Factors
# ---------------------------------

if r % 2 == 0:
    factor1 = gcd((a**(r // 2)) - 1, N)
    factor2 = gcd((a**(r // 2)) + 1, N)

    print("Factors of", N, "are:", factor1, "and", factor2)

else:
    print("Odd period found. Try another a")