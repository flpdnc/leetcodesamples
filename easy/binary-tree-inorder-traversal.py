class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    """
    If current does not have left child

        a. Add current’s value
    
        b. Go to the right, i.e., current = current.right

    Else

        a. In current's left subtree, make current the right child of the rightmost node

        b. Go to this left child, i.e., current = current.left
    """
    res = []
    curr = root
    stack = []
    if root is None:
        return res

    while curr is not None or len(stack) > 0:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right

    return res


import unittest

class TestInorderTraversal(unittest.TestCase):

    def test_first_sample(self):
        root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
        self.assertEqual(inorderTraversal(root), [1,3,2])

    def test_second_sample(self):
        root = None
        self.assertEqual(inorderTraversal(root), [])

    def test_third_sample(self):
        root = TreeNode(val=1)
        self.assertEqual(inorderTraversal(root), [1])

    def test_fourth_sample(self):
        root = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=None)
        self.assertEqual(inorderTraversal(root), [2,1])

    def test_fourth_sample(self):
        root = TreeNode(val=2, left=TreeNode(val=3, left=TreeNode(val=1, left=None, right=None), right=None), right=None)
        self.assertEqual(inorderTraversal(root), [1,3,2])

if __name__ == '__main__':
    unittest.main()
