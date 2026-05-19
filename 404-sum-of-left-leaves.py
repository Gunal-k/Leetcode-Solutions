class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node,flag):
            ans = 0
            if not node:
                return 0
            elif not node.left and not node.right:
                return node.val if flag else 0
            ans += dfs(node.left, True)
            ans += dfs(node.right, False)
            return ans
        
        return dfs(root,False)