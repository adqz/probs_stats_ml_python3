from collections import defaultdict

class RandomVariables:
	def __init__(self):
		pass
	
	def sum_equals_seven(self):
		''' This functions calculates the prob that sum of two dice equals 7 '''
		
		# generate dict where key is dice result and value is sum of the dice result
		d = { (i,j): i+j for i in range(1,7) for j in range(1,7)}
		
		# generate inverse key, value pairs so now key is sum and value is all combos that give that sum
		d_inv = defaultdict(list)
		for i,j in d.items():
			d_inv[j].append(i)

		prob_of_seven = len(d_inv[7])/len(d)
		print('Prob that sum equals seven = {0:.4f}'.format(prob_of_seven))




if __name__ == '__main__':
	rv = RandomVariables()
	rv.sum_equals_seven()
