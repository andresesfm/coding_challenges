import unittest

class Node(object):
    def __init__(self,key, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        self.key = key

    def push(self,node):
        self.left = node
        node.right = self

    def __str__(self):
        return f'({self.key})'
    
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.push(node)
            self.head = node

    def pop_last(self):
        if not self.tail:
            return None
        pop = self.tail
        ntail = self.tail.left
        if not ntail: #Means tail was == head 
            self.head = None
        else:
            ntail.right = None
        self.tail = ntail
        return pop

    def move_to_head(self, node):
        if node == self.head:
            return
        right =  node.right
        left = node.left
        currhead = self.head
        node.left = None
        node.right = currhead
        
        self.head = node
        currhead.left = node
        
        if right:
            right.left = left
        else: ## means it was the tail
            self.tail = left
        if left:
            left.right = right
        #fix tail
    
    def __str__(self):
        node = self.head
        s = []
        while node:
            s+= node.key
            node = node.right
        return '->'.join(s)
    
class TestQueue(unittest.TestCase):
    def test_add(self):
        q =Queue ()
        anode = Node('A','A1')
        q.add(anode)
        bnode = Node('B','B1')
        q.add(bnode)
        cnode = Node('C','C1')
        q.add(cnode)
        self.assertEqual('C->B->A', q.__str__())
        self.assertEqual(cnode, q.head)
        self.assertFalse(q.head.left)
        self.assertEqual(anode, q.tail)
        self.assertFalse(q.tail.right)

    def test_pop_last(self):
        q =Queue ()
        anode = Node('A','A1')
        q.add(anode)
        bnode = Node('B','B1')
        q.add(bnode)
        cnode = Node('C','C1')
        q.add(cnode)
        q.pop_last()
        self.assertEqual('C->B', q.__str__())
        self.assertEqual(cnode, q.head)
        self.assertFalse(q.head.left)
        self.assertEqual(bnode, q.tail)
        self.assertFalse(q.tail.right)

    def test_move_to_head(self):
        q =Queue ()
        anode = Node('A','A1')
        q.add(anode)
        bnode = Node('B','B1')
        q.add(bnode)
        cnode = Node('C','C1')
        q.add(cnode)
        q.move_to_head(bnode)
        self.assertEqual('B->C->A', q.__str__())
        self.assertEqual(bnode, q.head)
        self.assertFalse(q.head.left)
        self.assertEqual(anode, q.tail)
        self.assertFalse(q.tail.right)

    def test_move_to_head_last(self):
        q =Queue ()
        anode = Node('A','A1')
        q.add(anode)
        bnode = Node('B','B1')
        q.add(bnode)
        cnode = Node('C','C1')
        q.add(cnode)
        q.move_to_head(anode)
        self.assertEqual('A->C->B', q.__str__())
        self.assertEqual(anode, q.head)
        self.assertFalse(q.head.left)
        self.assertEqual(bnode, q.tail)
        self.assertFalse(q.tail.right)

##Implement Least Recently Used Algorithm for cache eviction
# https://www.youtube.com/watch?v=DUbEgNw-F9c
class LRU(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.hash = {}
        self.queue = Queue()
    
    def put(self,key,val):
        if len(self.hash) >= self.max_size:
            self.evict()
        nnode = Node(key,val)
        self.queue.add(nnode)
        self.hash[key] = nnode

    def get(self,key):
        #self.queue
        if not key in self.hash:
            return None
        found = self.hash[key]
        self.queue.move_to_head(found)
        return self.hash[key].val

    #Evicts the LRU element
    def evict(self):
        pop = self.queue.pop_last()
        del self.hash[pop.key]


class LRUTest(unittest.TestCase):
    def test_one_element(self):
        lru = LRU(1)
        lru.put('a','1')
        self.assertEqual(1,len(lru.hash))
        self.assertEqual('1',lru.get('a'))
        #should remain the same size
        lru.put('b','2')
        self.assertEqual(1,len(lru.hash))
        self.assertEqual(None,lru.get('a'))
        self.assertEqual('2',lru.get('b'))

    def test_multiple_elements(self):
        lru = LRU(5)
        lru.put('a','1')
        lru.put('b','2')
        lru.put('c','3')
        lru.put('d','4')
        lru.put('e','5')
        #refresh all but the last inserted one:
        lru.get('a')
        lru.get('b')
        lru.get('c')
        lru.get('d')
        lru.put('f','6')
        #e should be evicted by now

        self.assertEqual(5,len(lru.hash))
        self.assertEqual('f->d->c->b->a', lru.queue.__str__())
        self.assertEqual(None,lru.get('e'))
        self.assertEqual('1',lru.get('a'))
   

if __name__ == "__main__":
    unittest.main()