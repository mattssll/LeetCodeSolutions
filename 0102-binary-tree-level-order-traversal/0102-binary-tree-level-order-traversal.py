# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

from typing import Optional, List

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
