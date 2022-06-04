# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.rotate(root)
        return root
    
    def rotate(self,root):
        if root is None:
            return 
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp