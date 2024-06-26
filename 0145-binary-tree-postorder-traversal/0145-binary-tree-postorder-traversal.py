# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = list()
        stack = list()
        node = root
        maxi = 0
        
        while stack or node is not None:
            
            while node is not None:
                stack.append(node)
                ans.append(node.val)
                node = node.right
            node = stack.pop()
            node = node.left
        ans.reverse()
        return ans