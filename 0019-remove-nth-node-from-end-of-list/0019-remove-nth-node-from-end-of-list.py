# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        # skip the first N items, before we start with delayed one
        for _ in range(n):
            head = head.next

        # here update the delayed one aswell
        while head:
            head = head.next
            dummy = dummy.next
        
        # remove the item that is sopposed to be removed
        dummy.next = dummy.next.next

        return res.next

