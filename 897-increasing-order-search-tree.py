class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        ans = dummy
        def dfs(node):
            nonlocal ans
            if not node :
                return
            dfs(node.left)
            ans.right = TreeNode(node.val)
            ans = ans.right 
            dfs(node.right)
        dfs(root)
        return dummy.right
