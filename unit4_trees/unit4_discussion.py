"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The recursive method finds the correct spot for the new value.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If there is no node here, this is where the new value belongs.
        if node is None:
            return Node(value)

        # Smaller values go to the left side of the current node.
        # Larger values go to the right side.
        # This is what keeps the BST organized for easier searching.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the node so the tree connections stay in place.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A BST can usually find values faster than a regular list
        # because it can ignore one side of the tree at each step.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If there is no node left to check, the value is not there.
        if node is None:
            return False

        # The value was found.
        if value == node.value:
            return True

        # If the value is smaller, only search the left side.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # If the value is larger, only search the right side.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Stop when there is no node to visit.
        if node is None:
            return

        # Visit the left side first.
        self._inorder_recursive(node.left, values)

        # Add the current node after the left side.
        values.append(node.value)

        # Visit the right side last.
        self._inorder_recursive(node.right, values)

        # In a BST, smaller values are on the left and larger values
        # are on the right. Because of this order, the result is sorted.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Create an empty BST.
    tree = BST()

    # Insert several values into the tree.
    values = [50, 30, 70, 20, 40, 60, 80]

    for value in values:
        tree.insert(value)

    # Display the values that were added.
    print("Values inserted:", values)

    # A BST helps reduce the amount of data that needs to be checked.
    # At each step, we decide to go left or right instead of checking
    # every value in the tree.



    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # Get the values using an in-order traversal.
    ordered_values = tree.inorder()

    print("In-order traversal:", ordered_values)

    # The traversal checks left, then the current node, then right.
    # Since smaller values are on the left and larger values are on
    # the right, the values come out in sorted order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # These values are in the tree, so the search should return True.
    print("Search for 40:", tree.search(40))
    print("Search for 80:", tree.search(80))

    # These values are not in the tree, so the search should return False.
    print("Search for 25:", tree.search(25))
    print("Search for 100:", tree.search(100))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Test searching an empty tree.
    empty_tree = BST()

    # There are no nodes to search, so the result should be False.
    print("Search empty tree for 10:", empty_tree.search(10))

    # Test an empty tree's in-order traversal.
    # Since there are no nodes, the result should be an empty list.
    print("In-order traversal of empty tree:", empty_tree.inorder())



if __name__ == "__main__":
    main()