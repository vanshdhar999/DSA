"""This is an implementation of Binary Search algorithm. 
	
	Time Complexity: O(logn)
"""
import sys
sys.path.append('./Algorithms/')


import math
class BinarySearch():

	def __init__(self):

		self.TOL = 10e-7 # Define tolerance

	def binarysearch(self, lo, hi, target, function):

		assert lo <= hi, f'Lo can not be greater than hi !'

		mid = 0

		while (hi - lo) >= self.TOL:
			
			mid = (lo + hi) / 2

			value = function(mid)
			if value < target:
				lo = mid

			if value > target:
				hi = mid
			
			if value == target:

				return mid
		
		return mid

if __name__ == "__main__":

	# We can use binary search as a method to find the square root of any positive real number. Basically bisection method.

	your_function = lambda x: x * x # Lambda functions can be used to define anonymous functions

	lo = 0
	hi = 9801
	target = 9801
	bs = BinarySearch()
	sq_val = bs.binarysearch(lo, hi, target, your_function)
	print(f'Square root of {target} -> {sq_val}')



