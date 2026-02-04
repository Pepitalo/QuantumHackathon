#Fichier quantique

#Q1 To C or not to C
# THIS CELL IS PART OF THE SCORING CODE

from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.visualization import plot_gate_map

coupling_map = [
    (0, 1),
    (0, 2),
    (2, 3),
    (3, 4),
    (1, 4),
    (4, 5),
    (7, 5),
    (3, 6),
    (6, 7),
    (6, 8),
    (8, 9),
    (7, 10),
    (9, 10),
    (10, 11),
    (11, 13),
    (9, 12),
    (12, 13),
    (12, 14),
    (15, 14),
    (13, 16),
    (15, 16),
    (16, 17),
    (17, 19),
    (15, 18),
    (18, 19),
]
coupling_map += [(y, x) for (x, y) in coupling_map]

backend = GenericBackendV2(
    num_qubits=20,
    basis_gates=['id', 'rz', 'sx', 'x', 'cx', 'reset'],
    coupling_map=coupling_map
)
plot_gate_map(backend)

# SUBMISSION CELL
from qiskit import QuantumCircuit

qc = QuantumCircuit(20)
# YOUR CODE HERE



#Q2 : State preparation

#Q3 : Random state preparation

#Q4 : Send the lazy bit

#Q5 : Order, Order

#Q6 : Ansatz Design

#Q7 : A metrology question

#Q8 : Which state did I send
