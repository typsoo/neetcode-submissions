# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        d = {}

        def dfs(node, greater_than):
            if not node: return 0

            left_childs = dfs(node.left, greater_than)
            right_childs = dfs(node.right, greater_than + left_childs + 1)

            d[greater_than + left_childs] = node.val

            return left_childs + right_childs + 1

        dfs(root, 0)
        return d[k-1]