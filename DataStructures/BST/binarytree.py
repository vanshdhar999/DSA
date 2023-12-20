import sys

sys.path.append('./DataStructures/')

""" 
	Implementation of a binary search tree in python using classes. leftchild < parent < rightchild.
	All of the methods are defined in the Node class right now for simplicity.
"""
class Node:
	node_list = []
	def __init__(self, data: int):
		self.data = data
		self.rightchild = None
		self.leftchild = None

		Node.node_list.append(self.data)

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
	
	""" Tree traversals """
	def pre_order(self, node):

		if node:
			self.pre_order(node.leftchild)

			self.pre_order(node.rightchild)

			print(f'{node.data}', end = ' - ')
		
		
	def in_order(self, node):
		
		if node:
			self.in_order(node.leftchild)

			print(f'{node.data}', end = '  -  ')

			self.in_order(node.rightchild)

	def post_order(self, node):

		if node:

			print(f'{node.data}', end = ' - ')

			self.post_order(node.leftchild)

			self.post_order(node.rightchild)
	

	# Level order traversal using queue
	def level_order(self, root):
		
		queue = []

		if root is None:
			return f'Empty Tree'

		queue.append(root)

		while(len(queue) > 0):

			print(f'{queue[0].data}', end = ' - ')

			curr = queue.pop(0)

			if curr.leftchild is not None:
				queue.append(curr.leftchild)

			if curr.rightchild is not None:
				queue.append(curr.rightchild)

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.leftchild is not None or root.rightchild is not None:
            print_tree(root.leftchild, level + 1, "L--- ")
            print_tree(root.rightchild, level + 1, "R--- ")
		
if __name__ == "__main__":

	root = Node(100)
	bst_nodes = [50, 200, 40, 60, 150, 300]
	for node in bst_nodes:
		root.insert(root, node)
	print(f'BST Nodes -> {Node.node_list}')
	print_tree(root)




