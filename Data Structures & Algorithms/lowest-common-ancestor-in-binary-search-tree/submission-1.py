# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        res = root
        def dfs(root, mini, maxi):
            nonlocal res
            if not root: return

            if mini <= root.val <= maxi:
                res = root
                return
            
            if mini < root.val and maxi < root.val:
                dfs(root.left, mini, maxi)
            else:
                dfs(root.right, mini, maxi)

        dfs(root, min(p.val, q.val), max(p.val, q.val))
        

        return res


            