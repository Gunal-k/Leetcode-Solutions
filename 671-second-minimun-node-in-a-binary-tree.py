class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val = root.val
        def dfs(root):
            if not root:
                return -1

            if root.val > min_val:
                return root.val

            right = dfs(root.right)
            left = dfs(root.left)
            
            if left == -1:
                return right

            if right == -1:
                return left

            return min(left, right)
        return dfs(root)