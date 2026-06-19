class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans += abs(left-right)
            return root.val + left+right
        
        dfs(root)
        return self.ans
