# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1st solution with a set
        '''
        track = set()
        cur = head
        while cur:
            if cur in track:
                return True
            else:
                track.add(cur)
            cur = cur.next
        return False
        '''
        # Slow and fast pointer solution
        # why it works god knows... they end up meeting and so it happens
        slow = head
        fast = head
        # while fast.next makes sure that we don't go to the latest node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                return True