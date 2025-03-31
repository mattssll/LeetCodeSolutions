# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 1. recall urself to next val
        # 2. make your next the next of next
        # [4,5,1,9]
        node.val = node.next.val
        node.next = node.next.next