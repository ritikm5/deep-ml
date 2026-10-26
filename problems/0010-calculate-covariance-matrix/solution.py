
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n = len(vectors)
    N = len(vectors[0])

    # Calculate the mean of each feature
    means = [sum(v) / N for v in vectors]

    # Create the covariance matrix
    result = []

    for i in range(n):
        row = []
        for j in range(n):
            covariance = sum(
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(N)
            ) / (N - 1)

            row.append(float(covariance))

        result.append(row)

    return result
