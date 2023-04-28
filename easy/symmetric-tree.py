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
    if not root.left and not root.right:
        return True
    if (root.left and not root.right) or (root.right and not root.left):
        return False

    left_res = []
    left_curr = root.left
    left_stack = []

    while left_curr is not None or len(left_stack) > 0:
        while left_curr is not None:
            left_stack.append(left_curr)
            left_curr = left_curr.left
        left_curr = left_stack.pop()
        # In res, also have to keep track of depth, so each entry is tuple of
        # value and the current depth in the stack.
        left_res.append((left_curr.val, len(left_stack)))
        left_curr = left_curr.right

    right_res = []
    right_curr = root.right
    right_stack = []

    while right_curr is not None or len(right_stack) > 0:
        while right_curr is not None:
            right_stack.append(right_curr)
            right_curr = right_curr.right
        right_curr = right_stack.pop()
        right_res.append((right_curr.val, len(right_stack)))
        right_curr = right_curr.left

    if right_res == left_res:
        return True
    else:
        return False


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
