from qiskit import *
from qiskit_aer import *
# Quantum program setup




# Creating registers
q = QuantumRegister(3, 'q')
c0 = ClassicalRegister(1, 'c0')
c1 = ClassicalRegister(1, 'c1')
c2 = ClassicalRegister(1, 'c2')

# Creates the quantum circuit
teleport = QuantumCircuit(q, c0,c1,c2)

# Make the shared entangled state
teleport.h(q[1])
teleport.cx(q[1], q[2])

# Prepare Alice's qubit
teleport.h(q[0])

# Alice applies teleportation gates (or projects to Bell basis)
teleport.cx(q[0], q[1])
teleport.h(q[0])

# Alice measures her qubits
teleport.measure(q[0], c0[0])
teleport.measure(q[1], c1[0])

# Bob applies certain gates based on the outcome of Alice's measurements
teleport.z(q[2]).c_if(c0, 1)
teleport.x(q[2]).c_if(c1, 1)

# Bob checks the state of the teleported qubit
teleport.measure(q[2], c2[0])

simulator = Aer.get_backend('qasm_simulator')

# Transpile and assemble the circuit
transpiled_circuit = transpile(teleport, simulator)
qobj = assemble(transpiled_circuit, shots=1024)

# Run the algorithm
result = simulator.run(qobj).result()

#Shows the results obtained from the quantum algorithm
counts = result.get_counts(teleport)
print('\nThe measured outcomes of the circuits are:', counts)