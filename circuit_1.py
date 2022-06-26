"""Creating a circuit."""
# Define three qubits.
import cirq

a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")
c = cirq.NamedQubit("c")

# Define a list of operations.
ops = [cirq.H(a), cirq.H(b), cirq.CNOT(b, c), cirq.H(b)]

# Create a circuit from the list of operations.
circuit = cirq.Circuit(ops)
print("Circuit:\n")
print(circuit)

# Inspecting individual moments.
print("\nMoments in the circuit:\n")
for i, moment in enumerate(circuit):
    print('Moment {}: \n{}'.format(i, moment))

"""Print the repr of a circuit."""
print(repr(circuit))
