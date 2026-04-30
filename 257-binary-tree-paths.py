class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root,arr):
            if not root:
                return
            arr = arr + str(root.val)
            if not root.right and not root.left:
                ans.append(arr)
            else:
                dfs(root.left,arr + "->")
                dfs(root.right,arr + "->")
        dfs(root,"")
        return ans
    
        # def dfs(node, path):
        #     if not node:
        #         return
            
        #     path.append(str(node.val))
            
        #     if not node.left and not node.right:
        #         ans.append("->".join(path))
        #     else:
        #         dfs(node.left, path)
        #         dfs(node.right, path)
            
        #     path.pop()