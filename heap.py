class BinaryHeap():

	# Fast, efficient in time and space, implementation of binary heap
	# minimum heap

	#@staticmethod
	#def maxheap(a,b):
	#	return a > b

	#def minheap(a,b):
	#	return a < b

	#TODO - add support for maxheap

	def __init__(self, type=minheap):
		# we initialize it to [0], since we are filling up our heap as complete binary tree
		# from left to right, so for every node, index in array
		# left child is at 2*index, right child is at 2*index+1
		# the entire implementation is OBO if not for this dummy element
		# We can choose not to use zero as dummy element, but then left child is @ 2i+1, right child is at 2*i+2
		self.h = [0] 
		self.size = 0
		self.type = type # whether it is minheap or maxheap

	def peek(self):
		if self.isEmpty():
			return None
		return self.h[1]

	def __contains__(self, elem):
		return elem in self.h

	def heapifyDown(self, i):
		h = self.h

		# we have to check for i*2, because this node may not have any children
		# we actually end when 2*i (not i) is greater than h.size
		while (i*2) < self.size:
			# 
			index = self.getChildForSwap(i)
			# if we are greater than least child, then swap
			if h[i] > h[index]:

				self.swap(i, index)

			# multiply by 2 to get the next child, where we have swapped the element
			i = index

	def getChildForSwap(self, i):
		# to maintain our heap order property
		# we swap with node that is min(leftChild, rightChild)
		# so that the minimum value will be the new parent
		if 2*i+1 > self.size:
			return 2*i # we return left child if right is None

		#otherwise, we do comparison as normal and get min child
		if self.h[2*i] < self.h[2*i+1]:
			return 2*i
		else:
			return 2*i+1


	def delMin(self):
		# we delete the minimum, replace it with last element
		# then rearrange heap to maintain heap property
		h = self.h
		if h.isEmpty():
			return
		h[1] = h[-1]
		h.pop()
		self.size -= 1
		self.heapifyDown(self, 1)

	def isEmpty(self):
		return self.size == 1 # 1 for our dummy element

	def __len__(self):
		return self.size

	def buildHeap(self, a):
		# builds a new heap from a list of keys
		# could try inserting each element one by one
		# but that would be nlogn operations
		# logn to insert something in the heap for n elements
		# so decide to essentially rearrange the whole list in-place
		self.h = [0] + a[:]
		self.size = len(a)
		# we begin @ node in the middle of the array
		# because any nodes after this one will be leaves and have no children
		# so we want to heapify down for every node BEFORE THIS NODE
		i = len(a) // 2
		for i in range(len(a)//2, 0, -1):
			self.heapifyDown(i)

	def heapifyUp(self, i):
		h = self.h
		while i // 2 > 0:
			# if key is less than its parent, do basic swap
			if h[i] < h[i // 2]:
				self.swap(i//2, i)
			# this is how we get parent of current node
			i //= 2

	def insert(self, key):
		# insert a key into the heap
		# must satisfy the heap ordering property
		# every element is greater than or equal to its parent
		h = self.h
		h.append(key)
		self.size += 1
		i = self.size
		self.heapifyUp(self, i)


	def swap(self, i, j):
		# swap the values of two nodes
		temp = self.h[i]
		self.h[i] = self.h[j]
		self.h[j] = temp

	def __str__(self):
		return str(self.h)


	
if __name__ == '__main__':
	h = BinaryHeap()
	h.buildHeap(range(20,1,-1))
	print h
	#h = BinaryHeap()
	#for i in xrange(20,1,-1):
	#	h.insert(i)
	#print h