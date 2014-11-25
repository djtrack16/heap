heap
====

simple, fast, extensible-esque binary heap-like things

Binary heap implementation. Only supports minimum heap property for now. Minimum element can be accessed in constant time.

**Complexity**

- Insert: O(log n)
- Membership: O(n) (though checking for membership is usually not a priority in priority queues
- Delete Minimum: O(log n) (constant time to delete minimum, logn time to rearrange heap)
- Get Minimum: O(1) 
- Get Size: O(1)

**Usage:**

h = BinaryHeap()

**Builds a heap from the following list built by range**

h.buildHeap(range(20,-1,1))

**Insert element into heap**

h.insert(element)

TODO:

- Extend support for maximum heap property also.
- What about items that can/will carry multiple priorities?
- 
