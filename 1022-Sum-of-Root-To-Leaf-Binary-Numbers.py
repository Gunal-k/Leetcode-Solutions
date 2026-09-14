class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            if not node: return 0
            cur = cur*2+node.val
            if not node.right and not node.left: return cur
            return dfs(node.left, cur) + dfs(node.right, cur)
        return dfs(root, 0)
