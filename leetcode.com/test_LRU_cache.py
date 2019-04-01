import unittest

class Node:
    def __init__(self,key:int,val:int):
        self.left = None
        self.right = None
        self.key = key
        self.val = val
    def __str__(self):
        return f"{self.key},{self.val}"
    def __repr__(self):
        return self.__str__()
    
class DLQ:
    """
    Double linked list
    """
    def __init__(self):
        self.head =None
        self.tail = None
    
    def add(self,key,val):
        node = Node(key,val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.right = self.head
            self.head.left = node
            self.head = node
        return node
    
    def evict(self):
        if self.tail:
            if self.tail.left:
                tnode = self.tail
                lnode = self.tail.left
                self.tail = lnode
                tnode.left = None
                lnode.right = None
                return tnode
            else:
                tnode = self.tail
                self.tail = None
                return tnode
        return None
    
    def recent(self,node):
        if not node.left:
            #Nothing to do as this is the head already
            return node
        else:
            lnode = node.left
            rnode = node.right
            
            lnode.right = rnode
            
            if node == self.tail:
                self.tail = lnode
            else:
                rnode.left = lnode
            node.left = None
            node.right = None
            return self.add(node.key, node.val)

    def __str__(self):        
        curr = self.head
        s=""
        if curr:
            s = str(curr)
            while(curr.right):
                curr = curr.right
                s += "<->" + str(curr)
        else:
            s = "[]"
        return s

            

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.q = DLQ()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            cnode = self.cache[key]
            #rearrange queue
            nnode =self.q.recent(cnode)
            self.cache[key] = nnode
            return cnode.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #replace key
            enode = self.cache[key]
            enode.val = value
            nnode = self.q.recent(enode)
            self.cache[key] = nnode
            return
        elif len(self.cache) >= self.capacity:
            #evict item
            enode = self.q.evict()
            del self.cache[enode.key]
        #wrap in Node
        node = self.q.add(key,value)
        self.cache[key] = node
        
            
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class TestLRUcache(unittest.TestCase):
    def test_put(self):
        lru = LRUCache(2)
        lru.put(1,10)
        lru.put(2,20)
        lru.put(3,30)
        self.assertEqual(2,len(lru.cache))
        self.assertEqual(lru.cache[3].key,3)
        self.assertEqual(lru.cache[2].key,2)

    def test_get(self):
        lru = LRUCache(2)
        lru.put(1,10)
        self.assertEqual(lru.get(1),10)
        lru.put(2,20)
        lru.put(3,30)
        self.assertEqual(20,lru.get(2))
        self.assertEqual(30,lru.get(3))
        self.assertEqual(-1,lru.get(1))

    def test_example(self):
        lru =LRUCache(2)
        lru.put(1,1)
        lru.put(2,2)
        lru.get(1)
        lru.put(3,3)
        lru.get(2)
        lru.put(4,4)
        lru.get(1)
        lru.get(3)
        lru.get(4)

    def test_submit(self):
        lru = LRUCache(10)
        accs=["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
        params=[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
        for i,ac in enumerate(accs):
            #print(lru.q)
            #print(ac + "(" + ",".join(str(x) for x in params[i]) +")")
            if ac == "put":
                lru.put(params[i][0],params[i][1])
            else:
                lru.get(params[i][0])

    def test_submit2(self):
        lru = LRUCache(2)
        accs=["put","put","put","put","get","get"]
        params=[[2,1],[1,1],[2,3],[4,1],[1],[2]]
        expected = [None,None,None,None,-1,3]
        for i,ac in enumerate(accs):
            #print(lru.q)
            #print(ac + "(" + ",".join(str(x) for x in params[i]) +")")
            if ac == "put":
                lru.put(params[i][0],params[i][1])
            else:
                v = lru.get(params[i][0])
                self.assertEqual(expected[i],v)

    def test_submit3(self):
        lru = LRUCache(10)
        accs=["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
        params=[[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
        
        expected = [None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,-1,None,None,18,None,None,-1,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,-1,None,None,None,None,29,None,None,None,None,17,22,18,None,None,None,-1,None,None,None,20,None,None,None,-1,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
        for i,ac in enumerate(accs):
            print(lru.q)
            self.q_consistency(lru)
            print(lru.cache)
            print(ac + "(" + ",".join(str(x) for x in params[i]) +")")
            if ac == "put":
                lru.put(params[i][0],params[i][1])
            else:
                v = lru.get(params[i][0])
                self.assertEqual(expected[i],v)

    def q_consistency(self, lru: LRUCache):
        curr = lru.q.head
        arr_head = []
        if curr:
            arr_head.append(curr)
        while curr and curr.right:
            arr_head.append(curr.right)
            curr = curr.right

        curr = lru.q.tail
        arr_tail = []
        if curr:
            arr_tail.append(curr)
        while curr and curr.left:
            arr_tail.insert(0,curr.left)
            curr = curr.left
        self.assertEqual(arr_head,arr_tail)

        self.assertCountEqual(list(lru.cache.values()),arr_head)




class TestDLQ(unittest.TestCase):
    def test_add(self):
        q = DLQ()
        node = q.add(1,10)
        self.assertEqual(q.head,node)
        self.assertEqual(q.tail,node)
        node1 = q.add(2,20)
        self.assertEqual(q.head,node1)
        self.assertNotEqual(q.tail,node1)
        self.assertEqual(q.tail,node)

    def test_evict(self):
        q = DLQ()
        node1 = q.add(1,10)
        node2 = q.add(2,20)
        node3 = q.add(3,30)
        enode = q.evict()
        self.assertEqual(q.head,node3)
        self.assertEqual(q.tail,node2)
        self.assertTrue(enode)
        self.assertFalse(enode.right)
        self.assertFalse(enode.left)
        self.assertEqual(enode.val,node1.val)
        self.assertEqual(enode.key,node1.key)
        
        self.assertFalse(q.head.left)
        self.assertFalse(q.tail.right)
    
    def test_recent_middle(self):
        q = DLQ()
        node1 = q.add(1,10)
        node2 = q.add(2,20)
        node3 = q.add(3,30)
        q.recent(node2)
        self.assertEqual(node2.key, q.head.key)
        self.assertEqual(node2.val, q.head.val)
        self.assertEqual(node1,q.tail)

        self.assertFalse(q.head.left)
        self.assertFalse(q.tail.right)

    def test_recent_first(self):
        q = DLQ()
        node1 = q.add(1,10)
        node2 = q.add(2,20)
        node3 = q.add(3,30)
        q.recent(node3)
        self.assertEqual(node3.key, q.head.key)
        self.assertEqual(node3.val, q.head.val)
        self.assertEqual(node1,q.tail)

        self.assertFalse(q.head.left)
        self.assertFalse(q.tail.right)

    def test_recent_last(self):
        q = DLQ()
        node1 = q.add(1,10)
        node2 = q.add(2,20)
        node3 = q.add(3,30)
        q.recent(node1)
        self.assertEqual(node1.key, q.head.key)
        self.assertEqual(node1.val, q.head.val)
        self.assertEqual(node2,q.tail)

        self.assertFalse(q.head.left)
        self.assertFalse(q.tail.right)
        

if __name__ == "__main__":
    unittest.main()
    
