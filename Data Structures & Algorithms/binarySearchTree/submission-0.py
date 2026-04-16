class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        # inserting not necessarily recursive in BST
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        # recursively 
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr, key) -> TreeNode:
        # remove the node with key, return new root of subtree
        if not curr:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                # actual deletion of current node
                # swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderHelper(self.root, result)
        return result
    
    def inorderHelper(self, root, result):
        if root:
            self.inorderHelper(root.left, result)
            result.append(root.key)
            self.inorderHelper(root.right, result)

