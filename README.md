heap
====

Binary heap implementation, internally represented as a list. Only supports minimum heap property for now.

**Advantages**

n is number of keys in heap

- Priority element can be accessed in constant time.
- Rearranging after removing priority element takes time proportional to height of heap.
- Built as complete binary tree (levels in tree are filled from left to right), so heap height is always minimal.
- Heapsort can be done in-place with no (apparently) quadratic worst-case scenarios.
- Space efficient. A less memory-efficient, but more intuitive way: we could implement this as a binary tree, with every node having a link to its parent.

**Disadvantages**

* The keys are not strictly sorted: the only requirement is that the priority element is at the root. For instance, the median element may be near the bottom of the heap, so doing something like an in-order traversal would be non-trivial.
* I'm not aware of any other ones; please, inform me.


**Complexity**

- Insert: O(log n)
- Membership: O(n) (though checking for membership is usually not a priority in priority queues)
- Delete Minimum: O(log n) (constant time to delete minimum, logn time to rearrange heap)
- Get Minimum: O(1) 
- Get Size: O(1)
- Traversal: O(n)
- Validation: O(n) (say we wanted to validate if an array was in fact a heap. Strictly speaking, we would only have to traverse halfway through the array, because nodes after that are childless.)

**API**

h = Heap()

*Given a list of keys, builds a heap*

[All multiples of 3 from 1-999]

h.buildHeap(range(1000,-1,-3))

*Validation*

h.isValid(1, len(h)/2)

*Retrieval*

h.peek() - *Can I see the top element?*

h.getMin() - *Give it to me*

h.delMin() - *Delete it*

*Other*

"print h" will list each node with its left and right children, if you need a visual representation. It doesn't print childless nodes as they are already listed as children of previous elements.

TODO:

- Extend support for maximum heap property also.
- What about items that can/will carry multiple priorities/weights?
