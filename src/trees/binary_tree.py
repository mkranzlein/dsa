class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class NodeBinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def insert(self, val: int):
        """Inserts a node into the next available position."""
        if self.root is None:
            self.root = Node(val)
        node, insert_left = self.get_next_position()
        if insert_left:
            node.left = Node(val)
        else:
            node.right = Node(val)

    def insert_at(self, val: int, node: Node, insert_left: bool):
        """Inserts a value as the left or right child of a specified node."""
        if insert_left:
            if node.left is not None:
                raise RuntimeError("Position in tree is not available.")
            node.left = Node(val)
        else:
            if node.right is not None:
                raise RuntimeError("Position in tree is not available.")
            node.right = Node(val)

    def get_next_position(self) -> tuple[Node, bool]:
        """Returns next available position in tree.

        Next available position is the left-most position of the bottom of the
        tree or the left-most position on a new row.

        Returns:
            A tuple containing the parent node and a bool indicating whether
            the next position is the node's left child (True)
            or right child (False).
        """
        # What happens if no root?
        # If deepest node is right edge of level, how do you know you're at
        # right edge and need new level? Maybe traverse right to left?
        raise NotImplementedError

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

        # If just depth, could keep track of current depth or have external
        # max_depth variable, but want to return node too.

    def delete(self, node: Node):
        raise NotImplementedError
