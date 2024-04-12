from initialize import *
from qiskit import *


#initialize quantum program


my_alg = initialize(circuit_name = 'superdense', qubit_number=2, bit_number=2, backend = 'local_qasm_simulator', shots = 1024)

#add gates to the circuit

#creates a bell pair
my_alg.q_circuit.h(my_alg.q_reg[0]) # applies H gate to first qubit
my_alg.q_circuit.cx(my_alg.q_reg[0],my_alg.q_reg[1]) ## applies CX gate

#Alice encodes 01
my_alg.q_circuit.x(my_alg.q_reg[0])

#to measure in the Bell basis, Bob does the following operations before measuring in the standard basis
my_alg.q_circuit.cx(my_alg.q_reg[0],my_alg.q_reg[1]) ## applies CX gate
my_alg.q_circuit.h(my_alg.q_reg[0]) # applies H gate to first qubit
my_alg.q_circuit.measure(my_alg.q_reg[0], my_alg.c_reg[0]) # measures the first qubit
my_alg.q_circuit.measure(my_alg.q_reg[1], my_alg.c_reg[1]) # measures the second qubit


print('List of gates:')
for circuit in my_alg.q_circuit:
    print(circuit.name)

#Execute the quantum algorithm
result = my_alg.Q_program.execute(my_alg.circ_name, backend=my_alg.backend, shots= my_alg.shots)

#Show the results obtained from the quantum algorithm
counts = result.get_counts(my_alg.circ_name)

print('\nThe measured outcomes of the circuits are:', counts)