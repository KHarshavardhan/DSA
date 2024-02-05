#class to create doubly linked list
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    #create left and right nodes to maintain sequence from LRU to MRU left to right
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
 #remove from the list
    def remove(self,node):
        prv,nxt = node.prev,node.next
        prv.next,nxt.prev=nxt,prv 
#insert to the right of the DLL
    def insert(self,node):
        prv,nxt = self.right.prev,self.right
        prv.next=nxt.prev=node
        node.next,node.prev=nxt,prv
#if key is present in hashmap, it will remove the key,value from list and inserts the same key,value to the right for maintaing LRU - MRU. Finally returns the value of respective key else returns -1
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
#if key is present in hashmap, removes it and creates a new DLL , adds to hashmap and inserts the DLL to the right. if the length it over the capacity the lru is removed and deleted from the hashmap
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)