# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(ln, rn):
            if not ln and not rn: return True

            if ln and rn and ln.val == rn.val:
                return isSame(ln.left, rn.left) and isSame(ln.right, rn.right)

            return False


        def dfs(ln, rn):
            if not ln and not rn or not rn: return True
            if not ln: return False
        

            if isSame(ln, rn):
                return True
            
            return dfs(ln.right, rn) or dfs(ln.left, rn)

        return dfs(root, subRoot) 
