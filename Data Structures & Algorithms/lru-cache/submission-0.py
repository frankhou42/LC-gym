#LL Node contructor
class Node:
    #each nodes holds prev, next, key, value
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        #hashmap used for O(1) get method, to get any node
        self.hashmap = {}

        #LL used to track recently used and least used

        #tail node and head node used for O(1) remove and add
        
        #doubly LL used to implement the remove method, as it
        #easily allows me to see the previous node
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #class method needs self as param to know what is the calling obj
    def add(self, node: Node):
        #recently used node stored at head
        #use prev and next var for for intuitive insertion
        prev = self.head
        nxt = self.head.next

        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

        
    
    def remove(self, node: Node):
        #remove a node from any pos as for get method
        #we remove a node from anywhere to put it back in LL
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev




    def get(self, key: int) -> int:
        #Edge case: when key not in hashmap.
        #self.hashmap call just has all the keys
        if not key in self.hashmap:
            return -1

        node = self.hashmap[key]

        #move the node to front of LL, since its recently used
        self.remove(node)
        self.add(node)
        #no need to del from hashmap as order doesn't matter,
        #LL has the order covered
        return node.value 


    def put(self, key: int, value: int) -> None:

        #1. Remove node or dict key-value pair depending on cases

        #Case 1: key exists, remove the node, key-value pair intact as
        #it will be added back in
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        

        #2. Update/Add the key-value pair, add the node to LL
        # !prevent adding two nodes!
        self.hashmap[key] = Node(key, value)
        self.add(self.hashmap[key])

        #3. After adding the node and key-val pair if over cap, delete
        #Case 2: where hashmap larger than cap, remove last node, and key-value pair
        if len(self.hashmap) > self.cap:
            lastNode = self.tail.prev
            self.remove(lastNode)
            del self.hashmap[lastNode.key]


 
        


