from collections import deque


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class NodeBinaryTree:
    def __init__(self, root: Node = None) -> None:
        self.root = root

    def insert(self, val: int) -> None:
        """Inserts into next available position with breadth-first search."""
        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            node = queue.popleft()

            if node.left is None:
                node.left = Node(val)
                return
            if node.right is None:
                node.right = Node(val)
                return

            queue.append(node.left)
            queue.append(node.right)

    def insert_at(self, val: int, node: Node, insert_left: bool) -> None:
        """Inserts a value as the left or right child of a specified node."""
        if insert_left:
            if node.left is not None:
                raise RuntimeError("Position in tree is not available.")
            node.left = Node(val)
        else:
            if node.right is not None:
                raise RuntimeError("Position in tree is not available.")
            node.right = Node(val)

    def get_deepest_node(self, node: Node, depth: int) -> tuple[Node, int]:
        if node is None:
            return (None, 0)
        if node.left is None and node.right is None:
            return (node, depth)

        deepest_left, left_depth = self.get_deepest_node(node.left, depth + 1)
        deepest_right, right_depth = self.get_deepest_node(node.right, depth + 1)
        if right_depth > left_depth:
            return (deepest_right, right_depth)
        else:
            return (deepest_left, left_depth)

    def delete(self, node: Node):
        raise NotImplementedError

    def preorder_traversal(self) -> list[int]:
        """Traverses tree root, left, right, starting from root."""
        result = []
        def _preorder_traversal(root) -> None:
            if root is None:
                return
            result.append(root.val)
            _preorder_traversal(root.left)
            _preorder_traversal(root.right)
        
        _preorder_traversal(self.root)
        return result

    def inorder_traversal(self) -> list[int]:
        """Traverses tree left, root, right, starting from bottom left."""
        result = []
        def _inorder_traversal(root) -> None:
            if root is None:
                return
            _inorder_traversal(root.left)
            result.append(root.val)
            _inorder_traversal(root.right)
        
        _inorder_traversal(self.root)
        return result

    def postorder_traversal(self) -> list[int]:
        """Traverses tree left, right, root, starting from bottom left."""
        result = []
        def _postorder_traversal(root) -> None:
            if root is None:
                return
            _postorder_traversal(root.left)
            _postorder_traversal(root.right)
            result.append(root.val)

        _postorder_traversal(self.root)
        return result

    def level_order_traversal(self):
        raise NotImplementedError
