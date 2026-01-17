class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_successor(root, node_value):
    current = find_node(root, node_value)

    if not current:
        return None

    # If the node has a right child, the successor is the minimum
    # value node in the right subtree.
    if current.right:
        return find_min(current.right)

    # If the node doesn't have a right child, the successor is the
    # lowest ancestor whose left child is also an ancestor of the
    # current node.
    successor = None
    ancestor = root

    while ancestor != current:
        if current.value < ancestor.value:
            successor = ancestor
            ancestor = ancestor.left
        else:
            ancestor = ancestor.right

    return successor

def find_node(root, value):
    if not root:
        return None

    if value == root.value:
        return root

    if value < root.value:
        #if the value of node is greater than key. 
        # then left child is selected as it will be less than root node
        return find_node(root.left, value)
    else:
        return find_node(root.right, value)

def find_min(node):
    #since successor node will be the left child value  of right subtree
    while node.left:
        node = node.left
    return node.value


root = TreeNode(15)
root.left = TreeNode(10)
root.right = TreeNode(20)
root.left.left = TreeNode(5)
root.left.right = TreeNode(12)
root.right.right = TreeNode(25)

# Test cases
print(f'Successor of Node with Right Child {find_successor(root, 10)}')  
