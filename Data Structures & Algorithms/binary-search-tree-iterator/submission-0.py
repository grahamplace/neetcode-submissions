# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.path_stack: list[TreeNode] = []

        # Fill the stack by running an inorder DFS traversal
        self.explore(self.root)


    def explore(self, root: Optional[TreeNode]):
        if not root:
            return

        if root.right:
            self.explore(root.right)

        self.path_stack.append(root)

        if root.left:
            self.explore(root.left)
    def next(self) -> int:
        curr = self.path_stack.pop()
        return curr.val

    def hasNext(self) -> bool:
        return len(self.path_stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()