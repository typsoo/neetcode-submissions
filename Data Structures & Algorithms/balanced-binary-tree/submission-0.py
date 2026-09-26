# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        res = False
        def dfs(node):
            nonlocal res
            
            left = dfs(node.left) + 1 if node.left else 0
            right = dfs(node.right) + 1 if node.right else 0

            valid = abs(left -right) <= 1
            res = ( res or not valid)

            return max(left, right)       

        dfs(root)

        return not res
