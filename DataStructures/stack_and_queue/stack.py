'''
	Stack implementation, LIFO property.
	Insertion O(1)
	Deletion O(1)
'''

class Stack():

	def __init__(self):
		self.stack = []
		self.top = -1

	def __repr__(self):
		return f'{self.stack}'

	def push(self, val):
		self.top += 1
		self.stack.append(val)

		return 

	def is_empty(self):

		if self.top == -1:
			return f'Stack is Empty !'
	
	def pop(self):
		assert self.top >= 0, f'Underflow!'
		self.top -= 1
		return self.stack[self.top]

if __name__ == "__main__":
	s = Stack()
	for i in range(10):
		s.push(i)
		s.pop()
	print(s.is_empty())
