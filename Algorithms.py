
class Algorithms:
	def bubbleSort(list):
		for x in range(0, len(list)):
			for y in range(0, len(list)):
				if list[x] < list[y]:
					temp = list[x]
					list[x] = list[y]
					list[y] = temp