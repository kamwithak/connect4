class BinaryTreeNode(object):
    def __init__(self, left=None, right=None, val=-1):
        self.left = left
        self.right = right
        self.val = val

def inOrderTraversal(self, root=None):

    if (not root):
        return

    self.inOrderTraversal(root.left)
    print(root.val)
    self.inOrderTraversal(root.right)


if __name__ == '__main__':
    

    root = BinaryTreeNode(
        left=BinaryTreeNode(val=1),
        right=BinaryTreeNode(val=3),
        val=2
    )

    inOrderTraversal(root)
