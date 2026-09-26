# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = collections.deque([(p, q)])

        while dq:
            for _ in range(len(dq)):
                l, r = dq.popleft()

                if not l and not r: continue
                if not l or not r or l.val != r.val: return False

                dq.append((l.left, r.left))
                dq.append((l.right, r.right))

        return True





