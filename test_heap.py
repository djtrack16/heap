from heap import Heap
import random
import sys

''' We build an arbitrarily large heap, delete the minimum, and after every deletion
	we check whether the heap is still a heap. This is exhaustive, and not advisable
	in practice, but it's just a brute force way to be ruthless.

	heapifyUp(index) runs every time we insert a key
	heapifyDown(index) runs every time we delete a key (h.pop())
	we verify that h.pop() works by popping off minimum is actually minimum
	- then set minimum equal to just popped element
	h.pop() uses h.peek()
'''
def deleteAllAndRearrange(keys, size):
	minimum = -sys.maxint-1 # minimum int in python per sys documentation
	h = Heap()
	if keys:
		h.buildHeap(keys)
	else:
		for i in range(size,0,-1):
			h.insert(i)
	while not h.isEmpty():
		assert(h.isHeap())
		popped = h.pop()
		assert(minimum <= popped)
		minimum = popped


# shuffles a random array for any number of trials and builds a heap, then verifies it is a heap
def isHeapBuiltCorrectly(keys, trials):
	for i in xrange(trials):
		random.shuffle(keys)
		h = Heap()
		h.buildHeap(keys)
		assert(h.isHeap())

# can we make a valid heap with an array full of duplicates?
def duplicates(keys):
	deleteAllAndRearrange(keys, 0)


if __name__ == '__main__':
	for num in range(0,10000,678):
		deleteAllAndRearrange(None, num)
		print "%d keys deleted and rearranged successfully" % (num)

	keys = [5,55,6,6,6,6,3,3,2,2,8,8,9999]

	isHeapBuiltCorrectly(range(1,14321), 50)

	duplicates(keys)
