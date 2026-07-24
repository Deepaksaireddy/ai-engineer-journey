"""
Linear Algebra From Scratch (no NumPy)
---------------------------------------
Implements:
  1. vector_add(v, w)         -> element-wise vector addition
  2. dot_product(v, w)        -> scalar dot product of two vectors
  3. matrix_multiply(A, B)    -> matrix multiplication (list of lists)

Vectors are represented as flat lists: [1, 2, 3]
Matrices are represented as lists of row-lists: [[1, 2], [3, 4]]
"""

def vector_add(v, w):
    """
    Add two vectors of the same length, element by element.
    v, w : list[float]
    returns : list[float]
    """
    if len(v) != len(w):
        raise ValueError(f"Vectors must be the same length (got {len(v)} and {len(w)})")

    return [v[i] + w[i] for i in range(len(v))]

def dot_product(v, w):
    """
    Compute the dot product of two vectors: sum(v[i] * w[i] for all i).
    v, w : list[float]
    returns : float
    """
    if len(v) != len(w):
        raise ValueError(f"Vectors must be the same length (got {len(v)} and {len(w)})")

    total = 0
    for i in range(len(v)):
        total += v[i] * w[i]
    return total

def matrix_multiply(A, B):
    """
    Multiply matrix A (m x n) by matrix B (n x p), producing an (m x p) matrix.
    Each entry result[i][j] is the dot product of row i of A and column j of B.
    A : list[list[float]]  -- m rows, n columns
    B : list[list[float]]  -- n rows, p columns
    returns : list[list[float]]  -- m rows, p columns
    """
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError(
            f"Incompatible dimensions: A is {rows_A}x{cols_A}, B is {rows_B}x{cols_B}. "
            f"Columns of A must match rows of B."
        )

    # Initialize result matrix with zeros: rows_A x cols_B
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):          # for each row of A
        for j in range(cols_B):      # for each column of B
            # entry (i, j) = dot product of row i of A and column j of B
            row_i = A[i]
            col_j = [B[k][j] for k in range(rows_B)]
            result[i][j] = dot_product(row_i, col_j)
    return result


def print_matrix(M, label=""):
    """Pretty-print a matrix (list of lists) with an optional label."""
    if label:
        print(f"{label}:")
    for row in M:
        print("  ", row)
    print()

if __name__ == "__main__":
    # --- Vector addition ---
    v = [1, 2, 3]
    w = [4, 5, 6]
    print("Vector addition:")
    print(f"  {v} + {w} = {vector_add(v, w)}\n")

    # --- Dot product ---
    print("Dot product:")
    print(f"  {v} . {w} = {dot_product(v, w)}\n")

    # --- Matrix multiplication ---
    A = [
        [1, 2],
        [3, 4],
    ]
    B = [
        [5, 6],
        [7, 8],
    ]
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    print_matrix(matrix_multiply(A, B), "A x B")

    # Non-square example: (2x3) * (3x2) -> (2x2)
    C = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    D = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]
    print_matrix(C, "Matrix C (2x3)")
    print_matrix(D, "Matrix D (3x2)")
    print_matrix(matrix_multiply(C, D), "C x D (2x2)")
