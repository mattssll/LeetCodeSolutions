class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the process of merging.
        res = ListNode()
        cur = res
        
        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                # assign the next of our current node to incoming value
                cur.next = list1
                # advance our list of values by adding next to itself
                list1 = list1.next
            else:
                # assign the next of our current node to incoming value
                cur.next = list2
                # advance our list of values by adding next to itself
                list2 = list2.next
            cur = cur.next  # Move the cur (result list) pointer forward
        
        # If any list is still remaining, attach it directly
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        
        return res.next  # Skip the dummy node and return the merged list