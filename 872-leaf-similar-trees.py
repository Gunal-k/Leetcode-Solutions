class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,ans):
            if not root:
                return
            if not root.left and not root.right:
                ans.append(root.val)
            dfs(root.left,ans)
            dfs(root.right,ans)
            return ans
        ans1 = []
        ans2 = []
        return dfs(root1,ans1) == dfs(root2,ans2)
