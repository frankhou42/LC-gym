"""
use a doubly LL so that removing LRU node and adding MRU node is
O(1) when we access nodes. We then also uses a hashmap for the LL\
so taht we have O(1) access to the nodes in LL, enabling O(1) get and O(1) put.

Each node stores value, next and prev ptr
Hashmap has key as key, and the Node as value to modify LL
"""
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        #init LL
        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.next = self.last
        self.last.prev = self.first

        #init hashmap
        self.hashmap = {}

    def addMRU(self, node: Node):
        tmp = self.first.next
        self.first.next = node
        node.prev = self.first
        node.next = tmp
        tmp.prev = node
    
    #remove to just last, remove any node as when updating with
    #put or get method we may remove a node in middle of LL
    def removeNode(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        return node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            #only check capacity for put since we are adding

            #remove first then add so that we aren't removing the
            #wrong node as when we add first theres duplicate.
            self.removeNode(self.hashmap[key])
            self.addMRU(self.hashmap[key])
            return self.hashmap[key].val    
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            self.removeNode(self.hashmap[key])
            self.addMRU(self.hashmap[key])
            #no need to check capcity if we are just updating
        else:
            self.hashmap[key] = Node(key, value)
            self.addMRU(self.hashmap[key])
            if len(self.hashmap) > self.capacity:
                node = self.removeNode(self.last.prev)
                del self.hashmap[node.key]
