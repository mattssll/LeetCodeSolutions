class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Create a linked list: head -> ll1 -> ll2 -> ll3 -> ll4
ll1 = ListNode(2)
ll2 = ListNode(7)
ll3 = ListNode(1)
ll4 = ListNode(4)

# Linking the nodes
ll1.next = ll2
ll2.next = ll3
ll3.next = ll4

head = ll1  # The head of the list is ll1

# 2 > 7 > 1 > 4 
# remove the 7
def remove_node(n):
     n.val = n.next.val
     n.next = n.next.next
     

remove_node(ll2)
while head:
     print(head.val)
     head = head.next