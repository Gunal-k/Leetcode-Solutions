class Solution:
    def isCousins(self, root, x, y):

        info = {}

        def dfs(node, parent, depth):
            if not node:
                return

            if node.val == x or node.val == y:
                info[node.val] = (parent, depth)

            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)

        px, dx = info[x]
        py, dy = info[y]

        return dx == dy and px != py
