# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxi):
            if not node: return 0

            cnt = 0
            if node.left: cnt += dfs(node.left, max(maxi, node.val))
            if node.right: cnt += dfs(node.right, max(maxi, node.val))

            return cnt + int(node.val >= maxi)

        return dfs(root, -101)


        