''' Queue Implementation, FIFO property. Constant time operations. '''



class Queue():

	def __init__(self, n: int):
		self.queue = n*[0]
		self.len = n
		self.head = 0
		self.tail = 0
	def __repr__(self):
		return f'{self.queue}'

	def Enqueue(self, val):

		if self.tail == self.len:
			self.tail = 0

		self.queue[self.tail] = val

		self.tail += 1

	def Dequeue(self):

		if self.head == self.tail + 1:
			raise Exception(f'Underflow!')

		val = self.queue[self.head]

		if self.head == self.len:
			self.head = 1

		else:
			self.head += 1

		return val

	def is_empty(self):
		if self.head == self.tail:
			return f'Queue is Empty!'
if __name__ == '__main__':
	q = Queue(10)
	for i in range(10):
		q.Enqueue(i)
		q.Dequeue()
	print(q.is_empty())



