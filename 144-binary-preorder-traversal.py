class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:  
        curr, stack = root, []
        res = []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res