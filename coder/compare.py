def compare(solution, result):
		is_same = True
		for line1, line2 in zip(solution, result):
			if line1 != line2:
				is_same = False
		return is_same