#Fichier quantique

#Q1 To C or not to C
# THIS CELL IS PART OF THE SCORING CODE

from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.visualization import plot_gate_map
from qiskit import QuantumCircuit
import numpy as np

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

qc = QuantumCircuit(20)
qc.h(0)
qc.cx(0,1)
qc.swap(1, 4)
qc.swap(4, 5)
qc.swap(5,7)
qc.swap(7,10)
qc.swap(10,11)
qc.swap(11,13)
qc.swap(13,16)
qc.swap(16,17)
qc.swap(17,19)
qc.draw()
# YOUR CODE HERE



#Q2 : State preparation

# Note: you can change the number of qubits, but don't change the name of the quantum circuit
qc = QuantumCircuit(5)
qc.u(np.pi/2, 0, np.pi, 0)
qc.u(np.pi/2, 0, np.pi, 1)
qc.u(np.pi/2, 0, np.pi, 2)
qc.cx(0,4)
qc.cx(1,4)
qc.cx(2,4)
qc.cx(0,3)
print(qc.depth())
qc.draw()

#Q3 : Random state preparation

# YOUR CODE HERE
qc = QuantumCircuit(2)
qc.rx(lam * 2 * 71 *np.pi, 0)
qc.rz(lam * 2 * 143 *np.pi, 1)
qc.cx(0,1)
qc.ry(lam * 2 * (78963986129873600283%17) *np.pi, 0)
qc.rx(lam * 2 * (7629863912983710296496982198730192783897%172) *np.pi, 1)
qc.cx(1,0)
qc.rx(lam * 2 * 77398291 *np.pi, 1)
qc.rz(lam * 2 * 1409182033 *np.pi, 0)
qc.cx(0,1)
qc.ry(lam * 2 * (7896398612987363123800283%13) *np.pi, 1)
qc.rx(lam * 2 * (762986391298371923910923090296496982198730192783897%131) *np.pi, 0)
qc.cx(1,0)
qc.rx(lam * 2 * 1298371 *np.pi, 0)
qc.rz(lam * 2 * 1412933 *np.pi, 1)
qc.cx(0,1)
qc.ry(lam * 2 * (78912368712663986129873600283%17) *np.pi, 0)
qc.rx(lam * 2 * (76298639982137961239091283129837102964969821987301981927838992639877%312) *np.pi, 1)
qc.cx(1,0)
qc.draw("mpl")
# Resultat de ce test est 0.018, amélioration possible : on intrique selon plus que cx, mais ausi cy et cz
# Essai en tourant selon les 3 axes via une U gate, on garde le même nombre de gate du coup donc peut etre mieux
qc = QuantumCircuit(2)
qc.u(lam * 2 * 71 *np.pi,lam * 2 * 71 *np.pi,lam * 2 * 71 *np.pi, 0)
qc.u(lam * 2 * 143 *np.pi,lam * 2 * 143 *np.pi,lam * 2 * 143 *np.pi, 1)
qc.cx(0,1)
qc.u(lam * 2 * (78963986129873600283%17) *np.pi,lam * 2 * (78963986129873600283%17) *np.pi,lam * 2 * (78963986129873600283%17) *np.pi, 0)
qc.u(lam * 2 * (7629863912983710296496982198730192783897%172) *np.pi,lam * 2 * (7629863912983710296496982198730192783897%172) *np.pi,lam * 2 * (7629863912983710296496982198730192783897%172) *np.pi, 1)
qc.cx(1,0)
qc.u(lam * 2 * 77398291 *np.pi,lam * 2 * 77398291 *np.pi,lam * 2 * 77398291 *np.pi, 1)
qc.u(lam * 2 * 1409182033 *np.pi,lam * 2 * 1409182033 *np.pi,lam * 2 * 1409182033 *np.pi, 0)
qc.cx(0,1)
qc.u(lam * 2 * (7896398612987363123800283%13) *np.pi,lam * 2 * (7896398612987363123800283%13) *np.pi,lam * 2 * (7896398612987363123800283%13) *np.pi, 1)
qc.u(lam * 2 * (762986391298371923910923090296496982198730192783897%131) *np.pi,lam * 2 * (762986391298371923910923090296496982198730192783897%131) *np.pi,lam * 2 * (762986391298371923910923090296496982198730192783897%131) *np.pi, 0)
qc.cx(1,0)
qc.u(lam * 2 * 1298371 *np.pi,lam * 2 * 1298371 *np.pi,lam * 2 * 1298371 *np.pi, 0)
qc.u(lam * 2 * 1412933 *np.pi,lam * 2 * 1412933 *np.pi,lam * 2 * 1412933 *np.pi, 1)
qc.cx(0,1)
qc.u(lam * 2 * (78912368712663986129873600283%17) *np.pi,lam * 2 * (78912368712663986129873600283%17) *np.pi,lam * 2 * (78912368712663986129873600283%17) *np.pi, 0)
qc.u(lam * 2 * (76298639982137961239091283129837102964969821987301981927838992639877%312) *np.pi,lam * 2 * (76298639982137961239091283129837102964969821987301981927838992639877%312) *np.pi,lam * 2 * (76298639982137961239091283129837102964969821987301981927838992639877%312) *np.pi, 1)
qc.cx(1,0)
qc.draw("mpl")

#Q4 : Send the lazy bit

#Q5 : Order, Order

#Q6 : Ansatz Design

#Q7 : A metrology question

#Q8 : Which state did I send
