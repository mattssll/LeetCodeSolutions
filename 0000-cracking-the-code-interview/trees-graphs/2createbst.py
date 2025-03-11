class Node():
    def __init__(self, val, left= None, right=None):
        self.val = val
        self.left: Node = left
        self.right: Node = right
        print(val)
        

def create_bst_from_arr(arr, start, end):
    """
    We implement some sort of a binary search - 
    in every iteration we add mid element as the val of node
    and run create_bst to node.left and node.right by passing start and end params
    """
    # BST has left elements smaller than node and right elements bigger than node
    if (end < start):
        return None
    
    mid = (start+end) // 2
    node = Node(arr[mid])
    node.left = create_bst_from_arr(arr, start, mid-1)
    node.right = create_bst_from_arr(arr, mid+1, end)
    
    return node
 
# increasing sorted order with unique elements
arr = [1,4,7,9,10,13]
node = create_bst(arr, 0, len(arr)-1)
print(node)