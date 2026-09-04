class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        def dfs(root):
            if not root:
                return True
            nonlocal val
            if root.val != val:
                return False
            return dfs(root.left) and dfs(root.right)
        return dfs(root.left) and dfs(root.right)
