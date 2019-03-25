
# """

# GET:

# Should satisfy the below constraints:

# a) Get for key should return its value
# b) Accessing the key, should update its position in the recency map

# PUT:

# Should satisfy the below constraints:

# a) Add new key and value to the cache
# b) When capacity is reached we should be able to remove least used

# Design:

# If we use a hashmap to store the key and its value, it should satisfy the GET operation. How about updating its recency
# position in the map. If we use a stack then it might not be O(1). But if we use a doubly linked list, then everytime the
# key is accessed, we can retrieve its node from the hashmap (which will have the value) and the basically use
# the prev and next pointers to update the position. The current node should be made the head. And so if we could keep track of
# head and tail, it should help to update the tail's position or head's position when the nodes change. The size
# of the dictionary is the capacity.
# """


class LRUCache(object):
    class Node(object):
        def __init__(self, key, val):
            self.key, self.val, self.prev, self.next = key, val, None, None

    def __init__(self, capacity):
        self.capacity, self.hashmap = capacity, {}
        self.head, self.tail = self.Node(0, None), self.Node(0, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def updateHead(self, node):
        if node.key in self.hashmap:
            prev_node, next_node = node.prev, node.next
            prev_node.next, next_node.prev = next_node, prev_node
        next_node = self.head.next
        self.head.next, next_node.prev, node.prev, node.next = node, node, self.head, next_node

    def evictOldest(self):
        del self.hashmap[self.tail.prev.key]
        prev_node = self.tail.prev.prev
        prev_node.next, self.tail.prev = self.tail, prev_node

    def get(self, key):
        if key in self.hashmap:
            self.updateHead(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key, val):
        if key in self.hashmap:
            self.hashmap[key].val = val
            self.updateHead(self.hashmap[key])
        elif self.capacity:
            node = self.Node(key, val)
            self.updateHead(node)
            self.hashmap[key] = node
            if len(self.hashmap) > self.capacity: self.evictOldest()
