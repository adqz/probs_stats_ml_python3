from collections import defaultdict
from math import fsum
class RandomVariables:
	def __init__(self):
		# generate dict where key is dice result and value is sum of the dice result
		self.d = { (i,j): i+j for i in range(1,7) for j in range(1,7)}
		# generate inverse key, value pairs so now key is sum and value is all combos that give that sum
		self.d_inv = defaultdict(list)
		for i,j in self.d.items():
			self.d_inv[j].append(i)

	
	def sum_equals_seven(self):
		''' This functions calculates the prob that sum of two dice equals 7 '''
		
		prob_of_seven = len(self.d_inv[7])/len(self.d)
		print('Prob that sum equals seven = {0:.4f}'.format(prob_of_seven))

	def get_two_dice_pmf(self):
		''' Generates PMF of all results of two independent dice being cast '''

		X = {i:len(j)/len(self.d) for i,j in self.d_inv.items()}
		assert fsum(list(X.values())) == 1.0, 'probabilities must sum to 1'
		print('PMF is: \n', X)

	def sum_exceeds_half_of_product(self):
		''' For three dice, prob that half of the product will exceed their sum '''

		d = {(i,j,k): i*j*k/2 > i+j+k for i in range(1,7) for j in range(1,7) for k in range(1,7)}
		d_inv = defaultdict(list)
		for i,j in d.items():
			d_inv[j].append(i)
		X = {i: len(j)/len(d) for i,j in d_inv.items()}
		print('Probability that half of the product will exceed the sum is = {0:.4f}'.format(X[True]))




if __name__ == '__main__':
	rv = RandomVariables()
	rv.sum_equals_seven()
	rv.get_two_dice_pmf()
	rv.sum_exceeds_half_of_product()
