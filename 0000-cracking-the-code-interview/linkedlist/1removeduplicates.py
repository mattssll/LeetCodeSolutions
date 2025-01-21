class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Create a linked list: head -> ll1 -> ll2 -> ll3 -> ll4
ll1 = ListNode(2)
ll2 = ListNode(1)
ll3 = ListNode(1)
ll4 = ListNode(4)

# Linking the nodes
ll1.next = ll2
ll2.next = ll3
ll3.next = ll4

head = ll1  # The head of the list is ll1


def remove_duplicates(head):
     control = {}
     cur = head
     while cur and cur.next:  # We stop when cur.next is None
          if cur.next.val in control.keys():
               print('removing', cur.next.val)
               cur.next = cur.next.next  # remove next element from list
          else:
                control[cur.next.val] = 1
                cur = cur.next  # move to next element, 
                # This is the correct and intended behavior because it allows the current node 
                # to stay in place and the next node to be checked after a deletion.
          
          
          
# iterate in list and print
# Remove duplicates
remove_duplicates(head)

# Iterate through the list and print the values
res = head
while res:
    print(res.val)
    res = res.next

          