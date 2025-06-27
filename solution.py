from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        left_depth = 0
        right_depth = 0
        current = root

        def backtrack(current, depth, side): 
            if current:
                nonlocal left_depth, right_depth
                if side == "right":
                    if depth != right_depth or right_depth == 0:
                        result.append(current.val)
                    if depth >= right_depth:
                        right_depth = depth
                elif side == "left":
                    if depth > left_depth:
                        left_depth = depth
                    if depth > right_depth:
                        result.append(current.val)

                backtrack(current.right, depth + 1, "right")
                backtrack(current.left, depth + 1, "left")
        
        backtrack(current, 0, "right")

        return result