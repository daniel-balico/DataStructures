import unittest, io
import unittest.mock
from Algorithms import Algorithms
from DataStructures import (
	Stack, Queue, Tree, 
	TreeNode, LLNODE, LinkedList,
	DLL_Node, DoublyLinkedList)
import os

class TestAlgorithms(unittest.TestCase):
	algo = Algorithms()	

	# Check if bubble sort sorts correctly
	def test_bubbleSort(self):
		test_list = [5,4,3,2,1]
		sorted_list = [1,2,3,4,5]

		self.assertEqual(
			self.algo.bubbleSort(test_list), 
			sorted_list)

	# Check if selection sort sorts correctly
	def test_selectionSort(self):
		test_list = [5,4,3,2,1]
		sorted_list = [1,2,3,4,5]

		self.assertEqual(
			self.algo.selectionSort(test_list), 
			sorted_list)

	# Check if insertion sort sorts correctly
	def test_insertionSort(self):
		test_list = [5,4,3,2,1]
		sorted_list = [1,2,3,4,5]

		self.assertEqual(
			self.algo.insertionSort(test_list), 
			sorted_list)

	# Check if merge sort sorts correctly
	def test_mergeSort(self):
		test_list = [5,4,3,2,1]
		sorted_list = [1,2,3,4,5]

		self.assertEqual(
			self.algo.mergeSort(test_list), 
			sorted_list)

	# Check if quick sort sorts correctly
	def test_quickSort(self):
		test_list = [5,4,3,2,1]
		sorted_list = [1,2,3,4,5]

		self.assertEqual(
			self.algo.quickSort(test_list, 0, len(test_list)-1), 
			sorted_list)

	# Check if radix sort sorts correctly
	def test_radixSort(self):
		test_list = [5,4,3,2,1]
		sorted_list = [1,2,3,4,5]

		self.assertEqual(
			self.algo.radixSort(test_list), 
			sorted_list)

class TestDataStructures(unittest.TestCase):

	# Check is stack is working properly
	def test_stack(self):
		stack = Stack(5)

		# Check instantiation default values
		self.assertEqual(stack.data, [0,0,0,0,0])
		self.assertEqual(stack.top, -1)

		# Check if isEmpty() is Working
		self.assertTrue(stack.isEmpty())

		# Check if isFull() is Working
		self.assertFalse(stack.isFull())

		# Check if push() is working properly
		stack.push(10)
		self.assertEqual(stack.data, [10,0,0,0,0])

		# Check if count() is working properly
		self.assertEqual(stack.count(), 1)

		# Check isEmpty() again since it is not empty now
		self.assertFalse(stack.isEmpty())

		# Check if pop is working properly
		stack.pop()
		self.assertEqual(stack.data, [0,0,0,0,0])

		# Check count() again since there are no values now
		self.assertEqual(stack.count(), 0)


	def test_queue(self):
		queue = Queue(5)

		# Check instantiation default values
		self.assertEqual(queue.front, -1)
		self.assertEqual(queue.rear, -1)
		self.assertEqual(queue.length, 5)
		self.assertEqual(queue.data, [0,0,0,0,0])
		self.assertEqual(queue.count, 0)

		# Check if isEmpty()
		self.assertTrue(queue.isEmpty())
		# Check if isFull()
		self.assertFalse(queue.isFull())

		# Check if enqueue operation is working properly
		queue.enqueue(5)
		self.assertEqual(queue.data, [5,0,0,0,0])

		# Check count again if incremented
		self.assertEqual(queue.count, 1)

		# Check if front and rear is incremented
		self.assertEqual(queue.front, 0)
		self.assertEqual(queue.rear, 0)

		# Enqueue again to check if rear is working properly
		queue.enqueue(6)
		self.assertEqual(queue.rear, 1)
		self.assertEqual(queue.count, 2)

		# Check is countQueue() is working properly
		self.assertEqual(queue.countQueue(), 2)

		# Check if dequeue() is working properly
		queue.dequeue()
		self.assertEqual(queue.data, [0,6,0,0,0])
		self.assertEqual(queue.count, 1)


	# Check if SLL Nodes are working properly
	def test_SLLNode(self):
		node = LLNODE(5)
		self.assertEqual(node.value, 5)
		self.assertEqual(node.next, None)

	# Check if singly linked list is working properly
	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_SLL(self, mock_stdout):
		sll = LinkedList(5)

		# check default instantiation values
		self.assertEqual(sll.head.value, 5)
		self.assertEqual(sll.tail.value, 5)
		self.assertEqual(sll.tail.next, None)
		self.assertEqual(sll.length, 1)
		self.assertEqual(sll.count(), 1)

		# check if append() is working properly
		sll.append(6)
		self.assertEqual(sll.head.next.value, 6)
		self.assertEqual(sll.count(), 2)

		# check if prepend is working properly
		sll.prepend(4)
		self.assertEqual(sll.head.value, 4)
		self.assertEqual(sll.head.next.value, 5)
		self.assertEqual(sll.count(), 3)

		# check if traverse to index is working properly
		self.assertEqual(sll.traverseToIndex(1).value, 5)

		# check if insert() working properly
		sll.insert(1, 10)
		self.assertEqual(sll.head.next.value, 10)

		# Check if display() is working properly
		sll.display()
		self.assertEqual(mock_stdout.getvalue(), '4-->10-->5-->6-->\n')

		# Check if remove() is working properly
		sll.remove(5)
		self.assertEqual(sll.head.next.value, 10)

		# Test count() again
		self.assertEqual(sll.count(), 3)

	# Check if doubly linked list node is working properly
	def test_DLLNode(self):
		node = DLL_Node(5)
		self.assertEqual(node.value, 5)
		self.assertEqual(node.next, None)
		self.assertEqual(node.previous, None)
		
	# Check if Doubly Linked List is working properly
	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_DoublyLinkedList(self, mock_stdout):
		dll = DoublyLinkedList(10)

		# Check default instantiation values
		self.assertEqual(dll.head.value, 10)
		self.assertEqual(dll.tail.value, dll.head.value)
		self.assertEqual(dll.length, 1)

		# Check if append() is working properly
		dll.append(5)
		self.assertEqual(dll.head.next.value, 5)
		self.assertEqual(dll.head.next.previous.value, 10)
		self.assertEqual(dll.tail.next, dll.head)

		# Check if prepend() is working properly
		dll.prepend(2)
		self.assertEqual(dll.head.value, 2)
		self.assertEqual(dll.head.next.value, 10)
		self.assertEqual(dll.head.previous, None)

		# Check if display is working properly
		dll.display()
		self.assertEqual(mock_stdout.getvalue(), '2-->10-->5-->\n')

		# reset stdout
		mock_stdout.seek(0)
		mock_stdout.truncate(0)

		# Check if traverse to index is working properly
		self.assertEqual(dll.traverseToIndex(1).value, 10)

		# Check if insert is working properly
		dll.insert(1, 100)
		dll.display()
		self.assertEqual(mock_stdout.getvalue(), '2-->100-->10-->5-->\n')

		# reset stdout
		mock_stdout.seek(0)
		mock_stdout.truncate(0)

		# Check if remove is working properly
		dll.remove(10)
		dll.display()
		self.assertEqual(mock_stdout.getvalue(), '2-->100-->5-->\n')

	# Check if Node objects of tree is working properly
	def test_treeNode(self):
		treeNode = TreeNode(5)
		self.assertEqual(treeNode.value, 5)
		self.assertEqual(treeNode.left, None)
		self.assertEqual(treeNode.right, None)


	# Check if Tree Data structure is working properly
	@unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
	def test_tree(self, mock_stdout):
		bst = Tree()

		# Check if instantiation values are correct
		self.assertEqual(bst.root, None)
		self.assertEqual(bst.length, 0)

		# Check if insert is working properly
		bst.insert(10)
		self.assertEqual(bst.root.value, 10)
		bst.insert(9)
		self.assertEqual(bst.root.left.value, 9)
		bst.insert(11)
		self.assertEqual(bst.root.right.value, 11)
		bst.insert(12)
		self.assertEqual(bst.root.right.right.value, 12)
		bst.insert(8)
		self.assertEqual(bst.root.left.left.value, 8)

		# Check if inOrder Traversal is working properly
		bst.inOrder()
		self.assertEqual(mock_stdout.getvalue(), '8 9 10 11 12 ')

		# reset stdout
		mock_stdout.seek(0)
		mock_stdout.truncate(0)

		bst.preOrder()
		self.assertEqual(mock_stdout.getvalue(), '10 9 8 11 12 ')

		mock_stdout.seek(0)
		mock_stdout.truncate(0)

		# Check is postOrder Traversal is working properly
		bst.postOrder()
		self.assertEqual(mock_stdout.getvalue(), '8 9 12 11 10 ')


if __name__ == '__main__':
	unittest.main()