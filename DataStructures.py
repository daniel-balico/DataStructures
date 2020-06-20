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
		return self.top - 1


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
	def count(self):
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
		self.length = 0

	# Appending/Adding new Nodes to the end of the list
	def append(self, value):
		newNode = LLNODE(value)
		
		self.tail.next = newNode
		self.tail = newNode
		self.length = self.length + 1

	# Prepending/Adding new node to the start of the list
	def prepend(self, value):
		newNode = LLNODE(value)
		
		newNode.next = self.head
		self.head = newNode
		self.length = self.length + 1

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

		return currentNode

	# Insert a node in a given index in a list
	def insert(self, index, value):
		if index == 0:
			self.prepend(value)
		elif index == self.length:
			self.append(value)
		else:
			previousNode = self.traverseToIndex(index-1)
			newNode = Node(value)

			newNode.next = previousNode.next
			previousNode.next = newNode


	# Removing a node to the list
	def remove(self, item):
		currentNode = self.head

		while currentNode.next.value != item:
			currentNode = currentNode.next

		currentNode.next = currentNode.next.next
		self.length = self.length - 1

	# Returning the length of the list
	def count(self):
		return self.length+1

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

# To easily interact with the data structures
class Display:
	def DS_main(self):
		while True:
			# Display the available data structures
			print("\nDATA STRUCTURES \n\n Select a Data Structure: \n\n 1. Stack\n 2. Queue\n 3. Linked List\n 4. Binary Search Tree\n 5. Exit\n")

			try:
				selectedNumber = int(input("Select a number: "))
			except:
				print("\nPlease enter a valid input\n")
				input("Press [Enter] to continue...")
				self.DS_main()


			if selectedNumber == 1:
				self.DS_stack()
				break

			elif selectedNumber == 2:
				self.DS_queue()
				break

			elif selectedNumber == 3:
				self.DS_linkedlist()
				break

			elif selectedNumber == 4:
				self.DS_BST()
				break

			elif selectedNumber == 5:
				exit()
				break

	# Call the main method at instantiation
	def __init__(self):
		self.DS_main()

	def DS_stack(self):
		try:
			length = int(input("Enter the length of your Stack: "))
		except:
			return self.DS_stack()

		# Stack instantiation with the given length
		stack = Stack(length)

		while True:
			print('\n STACK OPERATIONS \n\n 1. Push\n 2. Pop\n 3. Display\n 4. Count\n 5. Back\n')

			try:
				selectedNumber = int(input("Select a number: "))
			except:
				print("\nPlease enter a valid input\n")
				input("Press [Enter] to continue...")
				self.DS_stack()

			if selectedNumber == 1:
				value = int(input("Enter the value that you want to push: "))
				stack.push(value)
				print("Success!")
				input("Press [Enter] to continue...")

			elif selectedNumber == 2:
				stack.pop()
				print("Success!")
				input("Press [Enter] to continue...")

			elif selectedNumber == 3:
				stack.display()
				input("Press [Enter] to continue...")

			elif selectedNumber == 4:
				stack.count()
				input("Press [Enter] to continue...")

			elif selectedNumber == 5:
				self.DS_main()

			else:
				print("The number you entered is not in the choices... Going back to the main screen instead...")
				input("Press [Enter] to continue...")
				self.DS_main()

	def DS_queue(self):
		try:
			length = int(input("Enter the length of your Queue: "))
		except:
			return self.DS_queue()

		# Queue instantiation with the given length
		queue = Queue(length)

		while True:
			print('\n QUEUE OPERATIONS \n\n 1. Enqueue\n 2. Dequeue\n 3. Display\n 4. Count\n 5. Back\n')
			
			try:
				selectedNumber = int(input("Select a number: "))
			except:
				print("\nPlease enter a valid input\n")
				input("Press [Enter] to continue...")
				self.DS_queue()

			if selectedNumber == 1:
				value = int(input("Enter the value that you want to enqueue: "))
				queue.enqueue(value)
				print("Success!")
				input("Press [Enter] to continue...")

			elif selectedNumber == 2:
				queue.dequeue()
				print("Success!")
				input("Press [Enter] to continue...")

			elif selectedNumber == 3:
				queue.display()
				input("Press [Enter] to continue...")

			elif selectedNumber == 4:
				queue.count()
				input("Press [Enter] to continue...")

			elif selectedNumber == 5:
				self.DS_main()

			else:
				print("The number you entered is not in the choices... Going back to the main screen instead...")
				input("Press [Enter] to continue...")
				self.DS_main()

	def DS_linkedlist(self):
		try:
			head = int(input("Enter the Head of your Linked List: "))
		except:
			return self.DS_queue()

		# Linked List instantiation with the given length
		linkedlist = LinkedList(head)

		while True:
			print('\n LINKED LIST OPERATIONS \n\n 1. Append\n 2. Prepend\n 3. Display\n 4. Count\n 5. Insert\n 6. Remove\n 7. Back\n')

			try:
				selectedNumber = int(input("Select a number: "))
			except:
				print("\nPlease enter a valid input\n")
				input("Press [Enter] to continue...")
				self.DS_linkedlist()

			if selectedNumber == 1:
				value = int(input("Enter the value that you want to append: "))
				linkedlist.append(value)
				print("Success!")
				input("Press [Enter] to continue...")

			elif selectedNumber == 2:
				value = int(input("Enter the value that you want to prepend: "))
				linkedlist.prepend(value)
				print("Success!")
				input("Press [Enter] to continue...")

			elif selectedNumber == 3:
				linkedlist.display()
				input("Press [Enter] to continue...")

			elif selectedNumber == 4:
				linkedlist.count()
				input("Press [Enter] to continue...")

			elif selectedNumber == 5:
				linkedlist.insert()
				print('Insert Complete')
				input("Press [Enter] to continue...")

			elif selectedNumber == 6:
				value = int(input("Enter the value that you want to remove: "))
				linkedlist.remove(value)
				print("Success!")
				input("Press [Enter] to continue...")

			elif selectedNumber == 7:
				self.DS_main()

			else:
				print("The number you entered is not in the choices... Going back to the main screen instead...")
				input("Press [Enter] to continue...")
				self.DS_main()

	def DS_BST(self):
		
		bst = Tree()

		while True:
			print('\n BST OPERATIONS \n\n 1. Insert\n 2. Traverse: PreOrder\n 3. Traverse: InOrder\n 4. Traverse: PostOrder\n 5. Back\n')

			try:
				selectedNumber = int(input("Select a number: "))
			except:
				print("\nPlease enter a valid input\n")
				input("Press [Enter] to continue...")
				self.DS_BST()

			if selectedNumber == 1:
				value = int(input("Enter the value that you want to insert: "))
				tree.insert(value)
				print("Insert Complete")
				input("Press [Enter] to continue...")

			elif selectedNumber == 2:
				tree.preOrder()
				input("Press [Enter] to continue...")

			elif selectedNumber == 3:
				tree.inOrder()
				input("Press [Enter] to continue...")

			elif selectedNumber == 4:
				tree.postOrder()
				input("Press [Enter] to continue...")

			elif selectedNumber == 5:
				self.DS_main()

			else:
				print("The number you entered is not in the choices... Going back to the main screen instead...")
				input("Press [Enter] to continue...")
				self.DS_main()



# Instantiate the display object
display = Display()
