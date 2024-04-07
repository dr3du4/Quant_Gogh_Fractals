from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram


qc = QuantumCircuit(3, 3)  # Alice, Bob, Psi

qc.h(0)
qc.rz(1.57, 0)


qc.h(1)
qc.cx(1, 2)


qc.cx(0, 1)
qc.h(0)
qc.measure([0, 1], [0, 1])


qc.cz(0, 2)
qc.cx(1, 2)


simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts(qc)


print("Wyniki teleportacji:")
print(counts)


plot_histogram(counts)


expected_state = {'000': 259}
teleported_state = counts


if teleported_state == expected_state:
    print(teleported_state)
    print(expected_state)
    print("Stan kwantowy został skutecznie przeteleportowany na qudit Boba.")
else:
    print(teleported_state)
    print(expected_state)
    print("Błąd: Stan kwantowy nie został poprawnie przeteleportowany.")

