class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def dfs(root):
            if not root:
                return
            freq[root.val] = freq.get(root.val,0)+1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        mx = max(freq.values())
        return [num for num in freq if freq[num] == mx]