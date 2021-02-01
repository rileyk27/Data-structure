# Data-structure
# 1. Bag
# 2. Hash
  * A data structure that stores data in a key
     - As data can be directly received through a key, the speed is dramatically increased.
     - A normal array is used after creating as much as the Hash Table size in advance
     - Python dictionary type is an example of hash table: directly retrieves data (value) with a key
  * Words
     - Hash: Converting an arbitrary value to a fixed length
     - Hash Table: A data structure that can be directly accessed by key value operation
     - Hashing Function: A function that can find the data location using arithmetic operations on the key.
     - Hash Value or Hash Address: By calculating the key with a hashing function, finding the hash value, and based on this, you can consistently find the data location for the key in the hash table.
     - Slot: Space to store one piece of data
There may be a separate function that can extract the key for the data to be saved.
  
# 3. Linked list

![link](https://user-images.githubusercontent.com/48328919/106408490-2d719f80-6404-11eb-8380-d08714ed8d5e.PNG)

* I build the linked list using c++, python language
# 4. Queue
  * FIFO (First-in, first-out), or LILO (Last-in, Last-out)
  * Enqueue: Input the data to Queue
  * Dequeue: Output the data at Queue
  
  ### In python laguage
   * Queue(): Most basic data structure
   * LifoQueue(): Last input data is first output
   * PriorityQueue(): Each data has priority, the height priority data is first output
   
# 5. Stack
  * Structure with limited access to data
     - Structure in which data can be inserted or removed only at one end
  * Data structure from which the last accumulated data can be pulled out first
     - Queue : FIFO policy
     - Stack : LIFO policy
  * Stack structure
     - The stack follows LIFO or FILO data management metods.
     - LIFO :Data management policy that extracts the last data first
     - FILO : Data management policy that extracts the data that was put first and last
     - Push() : push data onto the stack
     - pop() : pop data off the stack
  * Advantages
     - simple structure, easy to implement
  * Disadvantages
     - The maximum number of data must be determined in advance
     - In python, recursive functions can be called up to 1000 times
     - storage space may be wasted
     - The maximum number of storage spaces must be secured in advance
     
# 6. Tree

![tree](https://user-images.githubusercontent.com/48328919/106408474-264a9180-6404-11eb-9d4c-cdb719a59ab5.PNG)

 * A data structure constructed so as not to form a cycle by using nodes and branches
 * It is a structure in the form of a binary tree among trees, and is often used to implement search (search) algorithms.
 * Word
    - Node: The basic element that stores data in the tree (including data and branch information about other connected nodes)
    - Root Node: Node at the top of the tree
    - Level: When the highest node is Level 0, it indicates the depth of the node connected to the lower branch.
    - Parent Node: A node connected to the next level of a node
    - Child Node: A node connected to the upper level of a node
    - Leaf Node (Terminal Node): A node without any child nodes
    - Sibling (Brother Node): A node with the same Parent Node
    - Depth: The maximum level that a node can have in the tree.
     
# 7. Heap

![Heap](https://user-images.githubusercontent.com/48328919/106408407-0024f180-6404-11eb-8c5d-75342326d0e3.PNG)

 * Complete Binary Tree designed to quickly find the maximum and minimum values in the data.
 * Put the data on the heap, find the maximum and minimum values, then 𝑂(𝑙𝑜𝑔𝑛)
 * Heap structure
    - Heap can be classified into a structure for finding the maximum value (Max Heap) and a structure for finding the minimum value (Min Heap).
    - The value of each node is greater than or equal to the value of the child node of the node. 
    - In the case of the minimum heap, the value of each node is greater or less than the value of the child node of the node.
    - Has the form of a full binary tree
 * Commonalities and differences between heap and binary search tree
    - Common: Heap and binary search tree are both binary trees
    - Difference: In the heap, the value of each node is greater than or equal to the child node
    - Difference: There is no condition that a small value is left for a small value and a large value is right in a child node, which is a condition of a binary 
    - Difference: The value of the left and right child nodes of the heap may be large on the right or large on the left.
