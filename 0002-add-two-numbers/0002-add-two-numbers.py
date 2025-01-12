class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Convert the linked lists to integers
        mystr1 = ''
        cur1 = l1
        while cur1:
            mystr1 = str(cur1.val) + mystr1
            cur1 = cur1.next
        
        mystr2 = ''
        cur2 = l2
        while cur2:
            mystr2 = str(cur2.val) + mystr2
            cur2 = cur2.next
        
        # Step 2: Add the two numbers as integers
        result_str = str(int(mystr1) + int(mystr2))
        result_str = result_str[::-1]
        # Step 3: Build the result linked list
        dummy_head = ListNode(0)  # Create a dummy node to easily handle the head of the list
        current = dummy_head  # Pointer to build the new list
        
        for digit in result_str:
            current.next = ListNode(int(digit))  # Create a new node for each digit
            current = current.next  # Move the pointer to the next node
        
        return dummy_head.next  # Return the head of the result list (skip the dummy node)
