# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minValueNode(self, root) -> TreeNode:
        curr = root
        while curr and curr.left:
            curr = curr.left
        
        return curr
    
 
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # we are at deletion target
            if root.left is None and root.right is None: # 1a, 0 children
                return None
            elif root.left is not None and root.right is None: # 1a, left child only
                return root.left
            elif root.left is None and root.right is not None: # 1a, right child only
                return root.right
            else: # 2: 2 children
                min_value = self.minValueNode(root.right).val
                root.val = min_value
                root.right = self.deleteNode(root.right, min_value)
            
        return root
