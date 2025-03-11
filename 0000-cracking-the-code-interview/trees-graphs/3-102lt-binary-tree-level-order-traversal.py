'''
This consists of doing a BFS (since it is a level based approach) in a Tree.
We need a Queue, no need to have visited as we want to go to every member of tree, 
    no need to skip visited nodes, also tree has no visited nodes
For every level of the tree we store in list "res", the values of:
    for root tree: the value of the root node
    within while loop:
        value of node - no need to store for left and right since they will be added to queue in their respective turns
We start at level 0 and increase per iteration (or per call stack) the level in 1

We can't iterate in tree like we do with adjacency list in graphs:
    Our level is actually the size of the queue (dynamically we go one by one above)
In code:
for _ in range(level_is_len_q):
    # start dequeuing and go for neighbours
    ...
'''

from typing import Optional, List
import collections

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# RECURSIVE (SIMPLER)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []  # List to store the result
        self.treeBfs(root, 0)  # Start the recursive BFS from the root at level 0
        return self.res
    
    def treeBfs(self, node: TreeNode, level: int):
        if node is None:
            return
        
        # If this is the first time we've reached this level, we add a new sublist
        if len(self.res) == level:
            self.res.append([])
        
        # Add the current node's value to the corresponding level list
        self.res[level].append(node.val)
        
        # Recurse on left and right children with incremented level
        self.treeBfs(node.left, level + 1)
        self.treeBfs(node.right, level + 1)


# NON RECURSIVE
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.queue = collections.deque()
        self.res = []
        self.treeBfs(root, 0)
        return self.res
        
    
    def treeBfs(self, root, level):
        if root is None:
            return []
        # 1. add root to queue
        self.queue.append(root)

        while self.queue:
            level = len(self.queue)  # level is also the index from res
            self.res.append([])  # here we append the values from each level
            
            for _ in range(level):
            # start dequeuing and go for neighbours
                node = self.queue.popleft()
                self.res[level].append(node.val)  # appending tree root
                # send to queue if not None
                if node.left is not None:
                    self.queue.append(node.left)
                if node.right is not None:
                    self.queue.append(node.right)
            level+=1
        
        