
def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]] | int:
    # Check whether the dimensions align
    if len(a[0]) != len(b):
        return -1

    # Create the result matrix
    c = []

    # Loop through each row of matrix A
    for row in a:
        new_row = []

        # Loop through each column of matrix B
        for j in range(len(b[0])):
            # Calculate the dot product of the row and column
            total = 0
            for i in range(len(b)):
                total += row[i] * b[i][j]

            new_row.append(total)

        c.append(new_row)

    return c
