# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = None

        def dfs(node, greater_than):
            nonlocal res, k
            if not node: return 0

            left_childs = dfs(node.left, greater_than)
            right_childs = dfs(node.right, greater_than + left_childs + 1)

            if greater_than + left_childs == k - 1:res = node.val

            return left_childs + right_childs + 1

        dfs(root, 0)
        return res