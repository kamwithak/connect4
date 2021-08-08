class BinaryTreeNode(object):
    def __init__(self, left=None, right=None, val=-1):
        self.left = left
        self.right = right
        self.val = val

def inOrderTraversal(root=None):

    if (not root):
        return

    inOrderTraversal(root.left)
    print(root.val)
    inOrderTraversal(root.right)

if __name__ == '__main__':
    
    root = BinaryTreeNode(
        left=BinaryTreeNode(val=1),
        right=BinaryTreeNode(val=3),
        val=2
    )

    inOrderTraversal(root)
