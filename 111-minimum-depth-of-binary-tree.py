# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # level = 1
        if not root:
            return 0
        
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if not node.left and not node.right:
        #             return level
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        stack = [[root,1]]
        res = float('inf')

        while stack:
            node, depth = stack.pop()
            
            if not node.right and not node.left:
                res = min(res,depth)

            if node.right:
                stack.append([node.right,depth+1])
            if node.left:
                stack.append([node.left,depth+1])
        
        return res