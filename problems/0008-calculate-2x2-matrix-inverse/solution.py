def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here


    # Extract the four elements
    a, b = matrix[0]
    c, d = matrix[1]

    # Calculate the determinant
    det = a * d - b * c

    # If determinant is zero, inverse does not exist
    if det == 0:
        return None

    # Calculate and return the inverse matrix
    return [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
