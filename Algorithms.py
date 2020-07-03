class Algorithms:
	def bubbleSort(self, nums):
		for x in range(0, len(nums)):
			for y in range(0, len(nums)):
				if nums[x] < nums[y]:
					temp = nums[x]
					nums[x] = nums[y]
					nums[y] = temp

		return nums

	def selectionSort(self, nums):
		lengthOfNums = len(nums)

		for i in range(0, lengthOfNums):
			minimumVal = i
			temp = nums[i]

			for j in range((i+1), lengthOfNums):
				if nums[j] < nums[minimumVal]:
					minimumVal = j

			nums[i] = nums[minimumVal]
			nums[minimumVal] = temp

		return nums

	# https://www.geeksforgeeks.org/insertion-sort/
	def insertionSort(self, nums): 
	    for i in range(1, len(nums)): 
	        key = nums[i] 
	  
	        j = i-1
	        while j >=0 and key < nums[j] : 
	                nums[j+1] = nums[j] 
	                j -= 1

	        nums[j+1] = key

	    return nums

    # https://www.geeksforgeeks.org/merge-sort/
	def mergeSort(self, nums): 
		if len(nums) > 1: 
			mid = len(nums)//2 # Finding the mid of the list 
			L = nums[:mid] # Dividing the list elements  
			R = nums[mid:] # into 2 halves 

			self.mergeSort(L) # Sorting the first half 
			self.mergeSort(R) # Sorting the second half 

			i = j = k = 0

			# Copy data to temp lists L[] and R[] 
			while i < len(L) and j < len(R): 
				if L[i] < R[j]: 
					nums[k] = L[i] 
					i+= 1
				else: 
					nums[k] = R[j] 
					j+= 1
					k+= 1

			# Checking if any element was left 
			while i < len(L): 
				nums[k] = L[i] 
				i+= 1
				k+= 1

			while j < len(R): 
				nums[k] = R[j] 
				j+= 1
				k+= 1

		return nums

# QUICK SORT - https://www.geeksforgeeks.org/quick-sort

	# This function takes last element as pivot, places 
	# the pivot element at its correct position in sorted 
	# array, and places all smaller (smaller than pivot) 
	# to left of pivot and all greater elements to right 
	# of pivot 
	def partition(self, nums,low,high): 
	    i = ( low-1 )         # index of smaller element 
	    pivot = nums[high]     # pivot 
	  
	    for j in range(low , high): 
	  
	        # If current element is smaller than the pivot 
	        if   nums[j] < pivot: 
	          
	            # increment index of smaller element 
	            i = i+1 
	            nums[i],nums[j] = nums[j],nums[i] 
	  
	    nums[i+1],nums[high] = nums[high],nums[i+1] 
	    return ( i+1 )

	# Function to do Quick sort
	def quickSort(self, nums, low, high):
		if low < high: 
	        # pi is partitioning index, nums[p] is now 
	        # at right place 
			pi = self.partition(nums,low,high) 
	  
	        # Separately sort elements before 
	        # partition and after partition 

			self.quickSort(nums, low, pi-1) 

			self.quickSort(nums, pi+1, high)


			return nums

# RADIX SORT https://www.geeksforgeeks.org/radix-sort

	# A function to do counting sort of arr[] according to 
	# the digit represented by exp. 
	def countingSort(self, arr, exp1):
	    n = len(arr) 
	  
	    # The output array elements that will have sorted arr 
	    output = [0] * (n) 
	  
	    # initialize count array as 0 
	    count = [0] * (10) 
	  
	    # Store count of occurrences in count[] 
	    for i in range(0, n): 
	        index = (arr[i]/exp1) 
	        count[ int((index)%10) ] += 1
	  
	    # Change count[i] so that count[i] now contains actual 
	    #  position of this digit in output array 
	    for i in range(1,10): 
	        count[i] += count[i-1] 
	  
	    # Build the output array 
	    i = n-1
	    while i>=0: 
	        index = (arr[i]/exp1) 
	        output[ count[ int((index)%10) ] - 1] = arr[i] 
	        count[ int((index)%10) ] -= 1
	        i -= 1
	  
	    # Copying the output array to arr[], 
	    # so that arr now contains sorted numbers 
	    i = 0
	    for i in range(0,len(arr)): 
	        arr[i] = output[i]

	# Method to do Radix Sort 
	def radixSort(self, arr):
		max1 = max(arr)
		exp = 1
		while max1/exp > 0:
			self.countingSort(arr,exp)
			exp *= 10

		return arr