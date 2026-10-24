def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

	if len(a) >0 and len(a[0]) != len(b):
		return -1

	result = []

	for row in a:
		dot_pdt = sum(row[i] * b[i] for i in range(len(b)))
		result.append(dot_pdt)

	return result
	

	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass