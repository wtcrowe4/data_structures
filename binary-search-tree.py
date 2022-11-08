# Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
    def __str__(self):
        return str(self.root)
    def __repr__(self):
        return str(self.root)
    def printTree(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            self._printTree(self.root)
    def _printTree(self, curNode):
        if curNode is not None:
            self._printTree(curNode.left)
            print(curNode.data)
            self._printTree(curNode.right)
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)
    def _add(self, data, curNode):
        if data < curNode.data:
            if curNode.left is None:
                curNode.left = Node(data)
            else:
                self._add(data, curNode.left)
        elif data > curNode.data:
            if curNode.right is None:
                curNode.right = Node(data)
            else:
                self._add(data, curNode.right)
        else:
            print("Value already in tree")
    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None
    def _find(self, data, curNode):
        if data > curNode.data and curNode.right is not None:
            return self._find(data, curNode.right)
        elif data < curNode.data and curNode.left is not None:
            return self._find(data, curNode.left)
        if data == curNode.data:
            return curNode
    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None
    def delete(self, data):
        # returns true if node deleted
        # returns false if node to be deleted is not found
        if self.root is None:
            return False
        # find node containing data
        # get parent of node containing data
        parent = None
        node = self.root
        while node is not None and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
        if node is None:
            return False
        # get children count
        children_count = 0
        if node.left is not None:
            children_count += 1
        if node.right is not None:
            children_count += 1
        # break operation into different cases based on the
        # structure of the tree & node to be deleted
        # 1. delete node with no children
        if children_count == 0:
            if parent is not None:
                # break connection with parent
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        # 2. delete node with single child
        if children_count == 1:
            # get the single child node
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            if parent is not None:
                # replace the node to be deleted with its child
                if parent.left is node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
        # 3. delete node with two children
        if children_count == 2:
            # get the inorder successor of the deleted node
            parent_of_leftmost_node = node
            leftmost_node = node.right
            while leftmost_node.left is not None:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left
            # place the inorder successor in position of the node
            # to be deleted
            node.data = leftmost_node.data
            # fix the parent's left child
            if parent_of_leftmost_node.left == leftmost_node:
                parent_of_leftmost_node.left = leftmost_node.right
            else:
                parent_of_leftmost_node.right = leftmost_node.right
        return True
    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)
    def _findMin(self, node):
        if node.left is None:
            return node
        else:
            return self._findMin(node.left)
    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)
    def _findMax(self, node):
        if node.right is None:
            return node
        else:
            return self._findMax(node.right)
    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)
    def _height(self, node, cur_height):
        if node is None:
            return cur_height
        left_height = self._height(node.left, cur_height + 1)
        right_height = self._height(node.right, cur_height + 1)
        return max(left_height, right_height)
    def size(self):
        if self.root is None:
            return 0
        else:
            return self._size(self.root)
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
    def isBST(self):
        if self.root is None:
            return True
        else:
            return self._isBST(self.root, self.root.data)
    def _isBST(self, node, data):
        if node is None:
            return True
        if node.data < data:
            return False
        return self._isBST(node.left, node.data) and self._isBST(node.right, node.data)
    def isBalanced(self):
        if self.root is None:
            return True
        else:
            return (self._height(self.root.left) - self._height(self.root.right) <= 1)
    def isBalanced2(self):
        if self.root is None:
            return True
        else:
            return self._isBalanced2(self.root)
    def _isBalanced2(self, node):
        if node is None:
            return 0
        left_height = self._isBalanced2(node.left)
        if left_height == -1:
            return -1
        right_height = self._isBalanced2(node.right)
        if right_height == -1:
            return -1
        height_diff = left_height - right_height
        if abs(height_diff) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1
    def preorder(self):
        if self.root is not None:
            self._preorder(self.root)
    def _preorder(self, node):
        if node is not None:
            print(str(node.data))
            self._preorder(node.left)
            self._preorder(node.right)
    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(str(node.data))
            self._inorder(node.right)
    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)
    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(str(node.data))
    def levelorder(self):
        if self.root is not None:
            h = self._height(self.root, 0)
            for i in range(1, h + 2):
                self._printGivenLevel(self.root, i)
    def reverseLevelOrder(self):
        if self.root is not None:
            h = self._height(self.root, 0)
            for i in range(h, 0, -1):
                self._printGivenLevel(self.root, i)
    def _printGivenLevel(self, node, level):
        if node is None:
            return
        if level == 1:
            print(str(node.data))
        elif level > 1:
            self._printGivenLevel(node.left, level - 1)
            self._printGivenLevel(node.right, level - 1)
    def printGivenLevel(self, node, level):
        if node is None:
            return
        if level == 1:
            print(str(node.data))
        elif level > 1:
            self.printGivenLevel(node.left, level - 1)
            self.printGivenLevel(node.right, level - 1)
    def printLevelOrder(self):
        h = self.height()
        for i in range(1, h + 1):
            self.printGivenLevel(self.root, i)
    def printLevelOrder2(self):
        if self.root is None:
            return
        nodes = []
        nodes.append(self.root)
        while len(nodes) > 0:
            current_node = nodes.pop(0)
            print(str(current_node.data))
            if current_node.left is not None:
                nodes.append(current_node.left)
            if current_node.right is not None:
                nodes.append(current_node.right)
    def printLevelOrder3(self):
        if self.root is None:
            return
        nodes = []
        nodes.append(self.root)
        while len(nodes) > 0:
            current_node = nodes.pop(0)
            print(str(current_node.data))
            if current_node.left is not None:
                nodes.append(current_node.left)
            if current_node.right is not None:
                nodes.append(current_node.right)
    def printLevelOrder4(self):
        if self.root is None:
            return
        nodes = []
        nodes.append(self.root)
        while len(nodes) > 0:
            current_node = nodes.pop(0)
            print(str(current_node.data))
            if current_node.left is not None:
                nodes.append(current_node.left)
            if current_node.right is not None:
                nodes.append(current_node.right)
    def printLevelOrder5(self):
        if self.root is None:
            return
        nodes = []
        nodes.append(self.root)
        while len(nodes) > 0:
            current_node = nodes.pop(0)
            print(str(current_node.data))
            if current_node.left is not None:
                nodes.append(current_node.left)
            if current_node.right is not None:
                nodes.append(current_node.right)
    def traverse(self):
        if self.root is not None:
            self._traverse(self.root)
    def _traverse(self, node):
        if node is not None:
            self._traverse(node.left)
            self._traverse(node.right)
            print(str(node.data))
    def traverse2(self):
        if self.root is not None:
            self._traverse2(self.root)
    def _traverse2(self, node):
        if node is not None:
            self._traverse2(node.left)
            print(str(node.data))
            self._traverse2(node.right)
    
    
    
    
    
