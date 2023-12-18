

""" Implementation of a binary search tree in python using classes. leftchild < parent < rightchild"""

class Node:

	def __init__(self, data: int):
		self.data = data
		self.rightchild = None
		self.leftchild = None

	def __repr__(self):
		return f'{self.data}'

	def insert(self, node, elem):
		""" If key to be inserted is less than parent node, make leftchild otherwise rightchild. If key already exists, return Exception."""
		# Base case 
		if node == None:
			node = Node(elem)

		else:
			if elem < node.data:
				node.leftchild = self.insert(node.leftchild, elem)
			else:
				node.rightchild = self.insert(node.rightchild, elem)
		return node
if __name__ == "__main__":

	root = Node(2)
	root.insert(root, 1)
	root.insert(root, 3)
	root.insert(root, 4)
	root.insert(root, 5)
	root.insert(root, 6)
	root.insert(root, 7)

# nodes = int(input("Enter the number of nodes ->"))



