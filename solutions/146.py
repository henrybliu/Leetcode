class Node():
    def __init__(self, key=0, val=0, prev = None, nextNode = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nextNode = nextNode


class LRUCache:
    '''
    Use a linked list to represent our most LRU cache and a hashmap to store
    our recent keys. We can first initialize the LRU cache with garbage values.
    When "putting" on the cache, we remove from the end and add a new node.

    Time: O(n) for initialization, O(1) for get(), and O(1) for put()
    Space: O(n)
    '''

    def __init__(self, capacity: int):
        self.mapping= {}
        self.head = Node()
        self.tail = Node()

        
        dummy = self.head
        for i in range(capacity):
            newNode = Node(-1-i)
            dummy.nextNode = newNode
            newNode.prev = dummy
            dummy = dummy.nextNode
            self.mapping[-1-i] = dummy

        dummy.nextNode = self.tail
        self.tail.prev = dummy

    def get(self, key: int) -> int:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            return self.mapping[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.insert(self.mapping[key])
            #update the value
            self.mapping[key].val = value

        else:
            newNode = Node(key, value)
            self.insert(newNode)
            self.mapping[key] = newNode
            del self.mapping[self.head.nextNode.key]
            self.remove(self.head.nextNode)
        
    def remove(self, node):
        node.prev.nextNode = node.nextNode
        node.nextNode.prev = node.prev

    def insert(self, node):
        self.tail.prev.nextNode = node
        node.prev = self.tail.prev
        node.nextNode = self.tail
        self.tail.prev = node


        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)