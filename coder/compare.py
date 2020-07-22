def compare(solution, result):
	f1=open((str(solution)),mode = 'rb')
	f2=open((str(result)),mode = 'rb')
	for line1 in f1:
		for line2 in f2:
			if line1==line2:
				return True
			else:
				return False
			break
	f1.close()
	f2.close() 
