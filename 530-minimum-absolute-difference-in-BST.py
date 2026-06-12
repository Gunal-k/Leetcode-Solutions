# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        val = None
        def dfs(root):
            nonlocal val,ans
            if not root:
                return
            dfs(root.left)
            if val != None:
                ans = min(ans,abs(root.val-val))
            val = root.val
            dfs(root.right)
        dfs(root)
        return ans