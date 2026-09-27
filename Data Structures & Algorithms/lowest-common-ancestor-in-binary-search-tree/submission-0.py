# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        s = set()

        def dfs(root, target):
            if not root: return

            s.add(root.val)

            if target < root.val:
                return dfs(root.left, target)
            elif target > root.val:
                return dfs(root.right, target)
            else:
                return

        dfs(root, p.val)
        res = root
        
        def dfs2(root, target):
            nonlocal res
            if not root: return 

            if root.val in s:
                res = root
                if target < root.val:
                    return dfs2(root.left, target)
                elif target > root.val:
                    return dfs2(root.right, target)
                    
            return

        dfs2(root, q.val)
        return res


            