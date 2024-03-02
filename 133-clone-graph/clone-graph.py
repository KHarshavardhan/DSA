"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #create a hashmap to store the new nodes while creating them
        clone={}
        def copyNode(node):
            if node in clone:
                return clone[node]
            copy = Node(node.val)
            clone[node]=copy
            for n in node.neighbors:
                copy.neighbors.append(copyNode(n))
            return copy
        return copyNode(node) if node else None