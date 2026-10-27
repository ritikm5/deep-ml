import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    size = len(b)
    x = np.zeros(size)

    for _ in range(n):
        x_new = np.zeros(size)

        for i in range(size):
            total = sum(A[i][j] * x[j] for j in range(size) if j != i)
            x_new[i] = (b[i] - total) / A[i][i]

        x = x_new

    return np.round(x, 4).tolist()