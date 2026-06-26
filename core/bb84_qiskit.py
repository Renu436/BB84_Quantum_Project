import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()
rng = np.random.default_rng()

def run_bb84(n, attack=False):

    alice_bits = rng.integers(0, 2, n)
    alice_bases = rng.integers(0, 2, n)
    bob_bases = rng.integers(0, 2, n)

    bob_results = []

    for i in range(n):

        # Step 1: Alice prepares qubit
        qc = QuantumCircuit(1, 1)

        if alice_bits[i] == 1:
            qc.x(0)

        if alice_bases[i] == 1:
            qc.h(0)

        # Step 2: Eve (attack)
        if attack:
            eve_basis = rng.integers(0, 2)

            if eve_basis == 1:
                qc.h(0)

            qc.measure(0, 0)
            result = simulator.run(qc, shots=1).result()
            measured_bit = int(list(result.get_counts().keys())[0])

            # dddddddddddddddddddddddddddddddddd
            if rng.random() < 0.3:
                measured_bit = 1 - measured_bit

            # Eve resends
            qc = QuantumCircuit(1, 1)
            if measured_bit == 1:
                qc.x(0)
            if eve_basis == 1:
                qc.h(0)

        # Step 3: Bob applies basis
        if bob_bases[i] == 1:
            qc.h(0)

        # Step 4: Bob measures (ONLY ONCE)
        qc.measure(0, 0)
        result = simulator.run(qc, shots=1).result()
        measured_bit = int(list(result.get_counts().keys())[0])

        bob_results.append(measured_bit)

    # Step 5: Key generation
    alice_key = []
    bob_key = []

    for i in range(n):
        if alice_bases[i] == bob_bases[i]:
            alice_key.append(alice_bits[i])
            bob_key.append(bob_results[i])

    return np.array(alice_key), np.array(bob_key)