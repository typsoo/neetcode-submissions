# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque([root])

        res = []

        while q:
            nodes_list = []
            for _ in range(len(q)):
                node = q.popleft()

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

                nodes_list.append(node.val)
            res.append(nodes_list)

        return res

        