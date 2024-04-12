from qiskit import *

# Quantum program setup



Q_program = QuantumProgram()

# Creating registers
q = Q_program.create_quantum_register('q', 3)
c0 = Q_program.create_classical_register('c0', 1)
c1 = Q_program.create_classical_register('c1', 1)
c2 = Q_program.create_classical_register('c2', 1)

# Creates the quantum circuit
teleport = Q_program.create_circuit('teleport', [q], [c0,c1,c2])

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

# Shows gates of the circuit
circuits = ['teleport']
print(Q_program.get_qasms(circuits)[0])

# Parameters for execution on simulator
backend = 'local_qasm_simulator'
shots = 1024 # the number of shots in the experiment

# Run the algorithm
result = Q_program.execute(circuits, backend=backend, shots=shots)

#Shows the results obtained from the quantum algorithm
counts = result.get_counts('teleport')

print('\nThe measured outcomes of the circuits are:', counts)

# credits to:  https://github.com/QISKit/qiskit-tutorial