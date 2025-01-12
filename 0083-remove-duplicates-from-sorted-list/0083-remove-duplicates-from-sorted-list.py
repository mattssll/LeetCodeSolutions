class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Head is a pointer to first node
        current = head
        
        while current:
            # Check if current node value is equal to next node value
            while current.next and current.val == current.next.val:
                # Skip the duplicate node by updating the next pointer
                current.next = current.next.next
            # Move to the next node
            current = current.next
        
        return head