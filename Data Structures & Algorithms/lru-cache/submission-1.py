"""
a->c->b


"""


class Node: # !!!! takes in key and val
    def __init__(self, key, val):
        self.key = key
        self.val = val # the value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        #start and end keep track of start and end node, act as sentinel node
        self.start = Node(0,0)
        self.end = Node(0,0)
        self.start.next = self.end
        self.end.prev = self.start

    def add(self, node):
        #connect ot end of LL
        node.next = self.end
        node.prev = self.end.prev
        self.end.prev.next = node
        self.end.prev = node

    def remove(self, node):
        #disconnect node
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        #get the node and the value
        #re-put in this link list
        #if node not in return -1
        res = 0
        if key not in self.hashmap:
            return -1
        else:
            node = self.hashmap[key]
            res = node.val
            self.remove(node)
            self.add(node)
            #start->1->2->3->end
        
        return res

    def put(self, key: int, value: int) -> None:
        #if the key is new, then just add to end of LL
        #if we max out capacity, kick out the least recently used node put the new one at end of LL
        #if the key is in hashmap, update and put at end of LL
        node = Node(key, value)
        if key not in self.hashmap and len(self.hashmap) < self.cap:
            self.add(node)
            self.hashmap[key] = node
        
        elif key in self.hashmap:
            #remove the old node
            self.remove(self.hashmap[key])
            #add node to end of LL and hashmap
            self.add(node)
            self.hashmap[key] = node
        
        elif key not in self.hashmap and len(self.hashmap) == self.cap:
            LRUNode = self.start.next
            self.remove(LRUNode)
            del self.hashmap[LRUNode.key]
            self.add(node)
            self.hashmap[key] = node

# 3
# {1=node 2=node 3=node}
# 1->3->2