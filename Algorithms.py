
class Algorithms:
	def bubbleSort(numbers):
		for x in range(0, len(numbers)):
			for y in range(0, len(numbers)):
				if numbers[x] < numbers[y]:
					temp = numbers[x]
					numbers[x] = numbers[y]
					numbers[y] = temp

		return numbers