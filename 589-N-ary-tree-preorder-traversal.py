class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return

            ans.append(node.val)

            for child in node.children:
                dfs(child)

        dfs(root)
        return ans
