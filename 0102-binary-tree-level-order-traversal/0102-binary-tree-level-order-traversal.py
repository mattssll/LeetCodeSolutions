# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.visited = set()
        self.queue = collections.deque()
        self.res = []
        self.treeBfs(root, 0)
        return self.res
        
    
    def treeBfs(self, root, level):
        if root is None:
            return []
        # add to queue and visited
        self.queue.append(root)
        self.visited.add(root)

        while self.queue:
            len_q = len(self.queue)
            # here we append the values from each level
            self.res.append([])
            
            for _ in range(len_q):
            # start dequeuing and go for neighbours
                node = self.queue.popleft()
                self.res[level].append(node.val)  # appending tree root
                # handle left and right node
                if node.left is not None:
                    self.queue.append(node.left)
                if node.right is not None:
                    self.queue.append(node.right)
            level+=1  # go to next level
        
        