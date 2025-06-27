import unittest
from solution import Solution

# TreeNode definition for test purposes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Assuming the Solution class is implemented as follows:
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         ...

class TestRightSideView(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.sol.rightSideView(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.sol.rightSideView(root), [1])

    def test_full_tree(self):
        #       1
        #     /   \
        #    2     3
        #     \     \
        #      5     4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(self.sol.rightSideView(root), [1, 3, 4])

    def test_left_skewed_tree(self):
        #       1
        #      /
        #     2
        #    /
        #   3
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.sol.rightSideView(root), [1, 2, 3])

    def test_right_skewed_tree(self):
        #   1
        #    \
        #     2
        #      \
        #       3
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.sol.rightSideView(root), [1, 2, 3])
    
    def test_sparse_tree(self):
        #       1
        #     /   \
        #    2     3
        #     \   /
        #      5 6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(self.sol.rightSideView(root), [1, 3, 5])

if __name__ == "__main__":
    unittest.main()