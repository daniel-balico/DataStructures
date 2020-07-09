# [Fixed Length Stack]

class Stack:
	def __init__(self, length):
		self.top = -1
		self.data = []
		self.length = length

		# We are appending 0 to the Stack n of times
		index = 0
		while index != self.length:
			self.data.append(0)
			index = index + 1

	# Check if stack is Empty
	def isEmpty(self):
		if self.top == -1:
			return True

		return False

	# Check if stack is full
	def isFull(self):
		if self.top == self.length-1:
			return True

		return False

	# Display stack
	def display(self):
		index = self.length-1

		while index >= 0:
			print(f"ELEMENT[{index}] - ",self.data[index])
			index = index - 1

	# Push/add a value to the stack
	def push(self, value):
		if self.isFull():
			print("STACK OVERFLOW")
			return
		else:
			self.top = self.top + 1
			self.data[self.top] = value

	# Remove/Pop a value from the stack
	def pop(self):
		if self.isEmpty():
			print("STACK UNDERFLOW")
			return
		else:
			self.data[self.top] = 0
			self.top = self.top - 1

	# Return the number of elements in the stack
	def count(self):
		return self.top + 1


# [Circular Fixed Length Queue]

class Queue:
	def __init__(self, length):
		self.front = -1
		self.rear = -1
		self.length = length
		self.data = []
		self.count = 0

		# Append 0 to the queue n of times
		index = 0
		while index < self.length:
			self.data.append(0)
			index = index + 1

	# Check if queue is empty
	def isEmpty(self):
		if self.front == -1 and self.rear == -1:
			return True

		return False

	# Check if queue is full
	def isFull(self):
		if (self.rear+1)%self.length == self.front:
			return True

		return False

	# Display all the values in queue
	def display(self):
		print("\nQUEUE DATA STRUCTURE\n")

		print("FRONT - ", end="")
		for item in self.data:
			print(item, end=" ")

		print("- REAR \n")


	# Enqueue/add a value in queue
	def enqueue(self, value):
		if self.isFull():
			print("QUEUE IS FULL")
		elif self.isEmpty():
			self.front = 0
			self.rear = 0
		else:
			self.rear = (self.rear+1)%self.length

		self.data[self.rear] = value
		self.count = self.count + 1

	# Dequeue/remove a value in queue
	def dequeue(self):
		if self.isEmpty():
			print("QUEUE IS EMPTY")
			return
		elif self.front == self.rear:
			self.rear = -1
			self.front = -1
			return
		else:
			self.data[self.front] = 0
			self.front = (self.front+1)%self.length

		self.count = self.count - 1

	# Return the number of elements in the queue
	def countQueue(self):
		return self.count



# [Singly Linked List]

# SLL Node
class LLNODE:
	def __init__(self, value):
		self.value = value
		self.next = None

# Singly Linked List Object
class LinkedList:
	def __init__(self, value):
		self.head = LLNODE(value)
		self.tail = self.head
		self.length = 1

	# Appending/Adding new Nodes to the end of the list
	def append(self, value):
		newNode = LLNODE(value)
		
		self.tail.next = newNode
		self.tail = newNode
		self.length += 1

	# Prepending/Adding new node to the start of the list
	def prepend(self, value):
		newNode = LLNODE(value)
		
		newNode.next = self.head
		self.head = newNode
		self.length += 1

	# Displaying the nodes of the list
	def display(self):
		currentNode = self.head

		while currentNode != None:
			print(currentNode.value, end="-->")
			currentNode = currentNode.next

		print("")

	# Traverse to the given index
	def traverseToIndex(self, index):
		currentNode = self.head
		currentIndex = 0

		while currentIndex != index:
			currentNode = currentNode.next
			currentIndex += 1

		return currentNode

	# Insert a node in a given index in a list
	def insert(self, index, value):
		if index == 0:
			self.prepend(value)
		elif index == self.length:
			self.append(value)
		else:
			previousNode = self.traverseToIndex(index-1)
			newNode = LLNODE(value)

			newNode.next = previousNode.next
			previousNode.next = newNode

		self.length += 1


	# Removing a node to the list
	def remove(self, item):
		currentNode = self.head

		while currentNode.next.value != item:
			currentNode = currentNode.next

		currentNode.next = currentNode.next.next
		self.length = self.length - 1

	# Reverse a linked list
	def reverse(self):
		currentNode = self.head
		prev = None

		while currentNode:
			nextValue = currentNode.next
			currentNode.next = prev
			prev = currentNode
			currentNode = nextValue

		head = self.head
		tail = self.tail
		
		self.head = tail
		self.tail = head 

	# Returning the length of the list
	def count(self):
		return self.length


# [Circular Doubly Linked List]

# DLL Node
class DLL_Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.previous = None

# Doubly Linked List Object
class DoublyLinkedList:
	def __init__(self, value):
		self.head = DLL_Node(value)
		self.tail = self.head
		self.length = 1

	def append(self, value):
		newNode = DLL_Node(value)

		self.tail.next = newNode
		newNode.previous = self.tail
		self.tail = newNode
		self.tail.next = self.head

		self.length += 1

	def prepend(self, value):
		newNode = DLL_Node(value)

		newNode.next = self.head
		self.head.previous = newNode

		self.head = newNode
		
		self.length += 1

	def display(self):
		currentNode = self.head

		while currentNode != self.tail:
			print(currentNode.value, end="-->")
			currentNode = currentNode.next

		print(currentNode.value, end="-->")
		print("")


	def traverseToIndex(self, index):
		currentNode = self.head
		currentIndex = 0

		while currentIndex != index:
			currentNode = currentNode.next
			currentIndex += 1

		return currentNode

	def insert(self, index, value):
		if index == 0:
			self.prepend(value)
		elif index == self.length:
			self.append(value)
		else:
			previousNode = self.traverseToIndex(index-1)
			newNode = DLL_Node(value)

			newNode.next = previousNode.next
			previousNode.next.previous = newNode
			previousNode.next = newNode
			newNode.previous = previousNode

		self.length += 1

	# Removing a node to the list
	def remove(self, item):
		currentNode = self.head

		while currentNode.next.value != item:
			currentNode = currentNode.next

		currentNode.next = currentNode.next.next
		self.length = self.length - 1

	# Returning the length of the list
	def count(self):
		return self.length


# [Binary Search Tree]

# BST Nodes
class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# Binary Search Tree Object
class Tree:
	def __init__(self):
		self.root = None
		self.length = 0


	# Insert a node in the tree
	def insert(self, value):
		newNode = TreeNode(value)

		if self.root is None:
			self.root = newNode
			self.length = self.length + 1
		else:
			currentNode = self.root

			# Loop until it breaks
			while True:
				# If the given value is less than the current node value then go left
				if newNode.value < currentNode.value:
					if currentNode.left is None:
						currentNode.left = newNode
						self.length = self.length + 1
						break
					else:
						currentNode = currentNode.left

				# Go right
				else:
					if currentNode.right is None:
						currentNode.right = newNode
						self.length = self.length + 1
						break
					else:
						currentNode = currentNode.right

	# Inorder Traversal
	def inOrder(self):
		def init(root):
			if root:
				init(root.left)
				print(root.value, end=" ")
				init(root.right)

		return init(self.root)

	# PreOrder Traversal
	def preOrder(self):
		def init(root):
			if root:
				print(root.value, end=" ")
				init(root.left)
				init(root.right)

		return init(self.root)

	# Post Order Traversal
	def postOrder(self):
		def init(root):
			if root:
				init(root.left)
				init(root.right)
				print(root.value, end=" ")

		return init(self.root)