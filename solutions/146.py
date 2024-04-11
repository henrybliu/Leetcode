class Node:
    """
    Node class to keep track of which keys are MRU or LRU
    """

    def __init__(self, key=None, val=None, prevNode=None, nextNode=None):
        self.key = key
        self.value = val
        self.prev = prevNode
        self.next = nextNode


class LRUCache:
    """
    We use a doubly linked list to keep track of the MRU/LRU keys. Use a
    hashmap to retreive values associated with keys and locate whether a key
    should be evicted or not.

    Time: O(1)
    Space: O(n)
    """

    def __init__(self, capacity: int):
        # head is the MRU and tail is LRU
        self.head = Node()
        self.tail = Node()

        # use doubly linked to quickly grab LRU (tail) and MRU (head)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.k = capacity
        # holds the values for each key
        self.mapping = {}

    def get(self, key: int) -> int:
        # if the key exists, we need to have its node be MRU
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            return self.mapping[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if the key already exists, update its value
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            self.mapping[key].value = value
        # create a new node for this key
        else:
            # we are at or have exceeded capacity and should evict the LRU node
            if len(self.mapping) >= self.k:
                removed = self.remove(self.tail.prev)
                del self.mapping[removed.key]
            # create a new node
            self.mapping[key] = Node(key, value)
            self.insert(self.mapping[key])

    # always insert at the front
    def insert(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

    # removes the node and return it
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
