import numpy as np


class QRegister:
    def __init__(self, n_qbits, init):
        self._n = n_qbits
        assert len(init) == self._n

        self._data = np.zeros((2 ** self._n), dtype=np.complex64)
        self._data[int('0b' + init, 2)] = 1


a = QRegister(1, '0')    # |0>
b = QRegister(1, '1')    # |1>
c = QRegister(3, '010')  # |010>


def measure(self):
    probs = np.real(self._data) ** 2 + np.imag(self._data) ** 2
    states = np.arange(2 ** self._n)
    mstate = np.random.choice(states, size=1, p=probs)[0]
    return f'{mstate:>0{self._n}b}'


class QGate:
    def __init__(self, matrix):
        self._data = np.array(matrix, dtype=np.complex64)

        assert len(self._data.shape) == 2
        assert self._data.shape[0] == self._data.shape[1]

        self._n = np.log2(self._data.shape[0])

        assert self._n.is_integer()

        self._n = int(self._n)


def apply(self, gate):
    assert isinstance(gate, QGate)
    assert self._n == gate._n
    self._data = gate._data @ self._data

I = QGate([[1, 0], [0, 1]])
H = QGate(np.array([[1, 1], [1, -1]]) / np.sqrt(2))
X = QGate([[0, 1], [1, 0]])
Y = QGate([[0, -1j], [1j, 0]])
Z = QGate([[1, 0], [0, -1]])


def quantum_randbit():
    a = QRegister(1, '0')
    a.apply(H)

    return a.measure()


for i in range(32):
    print(quantum_randbit(), end='')
print()


def __matmul__(self, other):
    return QGate(np.kron(self._data, other._data))


def __pow__(self, n, modulo=None):
    x = self._data.copy()

    for _ in range(n - 1):
        x = np.kron(x, self._data)

    return QGate(x)


def U(f, n):
    m = n + 1

    U = np.zeros((2**m, 2**m), dtype=np.complex64)

    def bin2int(xs):
        r = 0
        for i, x in enumerate(reversed(xs)):
            r += x * 2 ** i
        return r

    for xs in product({0, 1}, repeat=m):
        x = xs[:~0]
        y = xs[~0]

        z = y ^ f(*x)

        instate = bin2int(xs)
        outstate = bin2int(list(x) + [z])
        U[instate, outstate] = 1

    return QGate(U)


def is_constant(f, n):
    q = QRegister(n + 1, '0' * n + '1')
    q.apply(H ** (n + 1))
    q.apply(U(f, n))
    q.apply(H ** n @ I)

    if q.measure()[:~0] == '0' * n:
        return True
    else:
        return False