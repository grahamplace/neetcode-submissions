from typing import Optional, List

class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class TreeMap:
    
    def __init__(self):
        self.root: Optional[TreeNode] = None


    def _insert(self, root: Optional[TreeNode], key: int, val: int) -> TreeNode:
        if root is None:
            return TreeNode(key, val)
        elif root.key < key: 
            root.right = self._insert(root.right, key, val)
        elif root.key > key:
            root.left = self._insert(root.left, key, val)
        else: # existing key: update value
            root.val = val

        return root

    def insert(self, key: int, val: int) -> None:
        self.root = self._insert(self.root, key, val)
        return

    def _binary_search(self, root, key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.key == key:
            return root
        elif root.key < key:
            return self._binary_search(root.right, key)
        else:
            return self._binary_search(root.left, key)

    def get(self, key: int) -> int:
        result = self._binary_search(self.root, key)
        return result.val if result else -1

    def getMin(self) -> int:
        curr = self.root
        if curr is None: return -1 

        while curr and curr.left:
            curr = curr.left

        return curr.val

    def getMax(self) -> int:
        curr = self.root
        if curr is None: return -1 

        while curr and curr.right:
            curr = curr.right

        return curr.val

    def _remove(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return
        
        if root.key < key:
            root.right = self._remove(root.right, key)
        elif root.key > key:
            root.left = self._remove(root.left, key)
        else: # this is the deletion target
            # case 1a: no children
            if root.left is None and root.right is None:
                return None
            # case 1b: 1 child
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            # case 2: 2 children
            elif root.left is not None and root.right is not None:
                # get min value of right subtree
                curr = root.right
                while curr and curr.left:
                    curr = curr.left
                
                root.key = curr.key
                root.val = curr.val
                root.right = self._remove(root.right, curr.key)

        return root
                

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _inorder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self._inorder(root.left) + [root.key] + self._inorder(root.right)

    def getInorderKeys(self) -> List[int]:
        return self._inorder(self.root)
