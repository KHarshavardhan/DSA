"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #hashmap to maintain the copies of original to traverse later
        copyFromOld = {None:None}
        cur = head
        #only create copy of original nodes and store the nodes in hashmap
        while cur:
            copy = Node(cur.val)
            copyFromOld[cur] = copy
            cur = cur.next
        cur =head
        #From hashmap bring all the copies and add next,random pointers from original
        while cur:
            copy = copyFromOld[cur]
            copy.next = copyFromOld[cur.next]
            copy.random = copyFromOld[cur.random]
            cur =cur.next
        #return the copy head 
        return copyFromOld[head]
