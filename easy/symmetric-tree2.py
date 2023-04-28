class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    """
    Keep track of each tree side, and compare.
    """
    # Single node, should be true.
    return isMirror(root, root)


def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.val == root2.val) and isMirror(root1.right, root2.left) and isMirror(root1.left, root2.right)
        


import unittest

class TestIsSymmetric(unittest.TestCase):

    def test_first_sample(self):
        root = TreeNode(
                val=1,
                left=TreeNode(
                    val=2,
                    left=TreeNode(
                        val=3,
                        left=None,
                        right=None),
                    right=TreeNode(
                        val=4,
                        left=None,
                        right=None)
                    ),
                right=TreeNode(
                    val=2,
                    left=TreeNode(
                        val=4,
                        left=None,
                        right=None),
                    right=TreeNode(
                        val=3,
                        left=None,
                        right=None)
                    )
                )
        self.assertEqual(isSymmetric(root), True)

    def test_second_sample(self):
        root = TreeNode(
                val=1,
                left=TreeNode(
                    val=2,
                    left=None,
                    right=TreeNode(
                        val=3,
                        left=None,
                        right=None)
                    ),
                right=TreeNode(
                    val=2,
                    left=None,
                    right=TreeNode(
                        val=3,
                        left=None,
                        right=None)
                    )
                )
        self.assertEqual(isSymmetric(root), False)

    def test_third_sample(self):
        root = TreeNode(val=1, left=None, right=None)
        self.assertEqual(isSymmetric(root), True)

    def test_fourth_sample(self):
        root = TreeNode(
                val=1,
                left=TreeNode(
                    val=2,
                    left=TreeNode(
                        val=2,
                        left=None,
                        right=None),
                    right=None),
                right=TreeNode(
                    val=2,
                    left=TreeNode(
                        val=2,
                        left=None,
                        right=None),
                    right=None)
                )
        self.assertEqual(isSymmetric(root), False)

    def test_fifth_sample(self):
        root = TreeNode(
                val=5,
                left=TreeNode(
                    val=4,
                    left=None, 
                    right=TreeNode(
                        val=1, 
                        left=TreeNode(
                            val=2,
                            left=None,
                            right=None
                            ),
                        right=None
                        )
                    ),
                right=TreeNode(
                    val=1,
                    left=None,
                    right=TreeNode(
                        val=4,
                        left=TreeNode(
                            val=2,
                            left=None,
                            right=None
                            ),
                        right=None
                        )
                    )
                )
        self.assertEqual(isSymmetric(root), False)


if __name__ == '__main__':
    unittest.main()
