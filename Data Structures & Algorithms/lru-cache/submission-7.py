class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        self.hashmap = {}  # key : Node!

        self.first = Node(0, 0)
        self.last = Node(0, 0)
        self.first.next = self.last
        self.last.prev = self.first

    def add(self, node):
        tmp = self.first.next

        self.first.next = node
        node.prev = self.first

        tmp.prev = node
        node.next = tmp

    def remove(self, node):
        tmp1 = node.prev
        tmp2 = node.next
        tmp1.next = tmp2
        tmp2.prev = tmp1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashmap:
            return -1

        val = self.hashmap[key].val

        # doubly LL
        node = self.hashmap[key]
        self.remove(node)
        self.add(node)

        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        # case 1: update val of key if key exists
        if key in self.hashmap:
            oldNode = self.hashmap[key]
            self.hashmap[key] = Node(key, value)

            # update d LL
            node = self.hashmap[key]
            self.remove(oldNode)
            self.add(node)
        else:  # case 2:
            self.hashmap[key] = Node(key, value)
            node = self.hashmap[key]

            if len(self.hashmap) > self.capacity:
                lastNode = self.last.prev
                self.remove(lastNode)
                del self.hashmap[lastNode.key]

            self.add(node)