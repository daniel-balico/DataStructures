from DataStructures import Stack, Queue, LinkedList, Tree
from Algorithms import Algorithms
import time

# To easily interact with the data structures
class Display:
	def main(self):
		while True:
			# Display the available data structures
			print("\nData Structures and Algorithms by Daniel Shan Balico \n\n Select a number: \n\n 1. Data Structures\n 2. Algorithms\n 3. Exit\n")

			try:
				selectedNumber = int(input("Select a number: "))
			except:
				print("\nPlease enter a valid input\n")
				input("Press [Enter] to continue...")
				self.main()

			if selectedNumber == 1:
				self.DS_main()
				break

			elif selectedNumber == 2:
				self.Algo_main()
				break

			else:
				exit()

	# Call the main method at instantiation to be called again later
	def __init__(self):
		self.main()

	# Data Structures ------------------------------------------------------
	def DS_main(self):
		while True:
			# Display the available data structures
			print("\nDATA STRUCTURES \n\n Select a Data Structure: \n\n 1. Stack\n 2. Queue\n 3. Linked List\n 4. Binary Search Tree\n 6. Back\n")

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

			elif selectedNumber == 6:
				self.main()


	# Stack
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

	# Queue
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

	# LinkedList
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

	# Binary Search Tree
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

	# Algorithms ------------------------------------------------------
	def Algo_main(self):
		while True:
			# Display the available data structures
			print("\nAlgorithms \n\n Select an Algorithm: \n\n 1. Bubble Sort\n 2. Insertion Sort\n 3. Merge Sort\n 4. Quick Sort\n 5. Back\n 6. Exit\n")

			try:
				selectedNumber = int(input("Select a number: "))
			except:
				print("\nPlease enter a valid input\n")
				input("Press [Enter] to continue...")
				self.Algo_main()

			# To exit application immediately before asking the list of numbers
			if selectedNumber == 6:
				exit()

			# Ask for a list of numbers to sort
			input_listOfNumbers = input("Enter a list of numbers splitted by ',' Ex. 1,3,4 with no spaces \n\n Enter here: ")
			try:
				listOfNumbers = input_listOfNumbers.split(",")
			except:
				print("Wrong Format")
				input("Press [Enter] to continue...")
				self.Algo_main()

			# Bubble Sort
			if selectedNumber == 1:
				start = time.time()
				sortedList = Algorithms.bubbleSort(listOfNumbers)
				result = time.time() - start

				print(f"Numbers are now sorted:\n\n {sortedList} \n\n Execution time = {result}")
				input("Press [Enter] to continue...")
				

			elif selectedNumber == 2:
				break

			elif selectedNumber == 3:
				break

			elif selectedNumber == 4:
				break

			elif selectedNumber == 5:
				self.main()
				break



# Instantiate the display object
display = Display()
