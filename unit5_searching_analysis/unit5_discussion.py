"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Check each item from the beginning to the end.
    # This is O(n) because the algorithm may need to check
    # every item in the list.
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:

        # Find the middle of the current search area.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:
            # Ignore the left half because the target is larger.
            left = middle + 1

        else:
            # Ignore the right half because the target is smaller.
            right = middle - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Small sorted dataset
    small_list = [10, 20, 30, 40, 50]

    # Test a value that exists
    target = 30
    print("Searching for:", target)
    print("Linear search result:", linear_search(small_list, target))
    print("Binary search result:", binary_search(small_list, target))

    # Test a value that does not exist
    target = 35
    print("\nSearching for:", target)
    print("Linear search result:", linear_search(small_list, target))
    print("Binary search result:", binary_search(small_list, target))

    # Both searches return -1 when the value is not found.


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Create a larger sorted dataset from 1 to 10,000
    large_list = list(range(1, 10001))

    target = 9999

    print("Searching for:", target)
    print("Linear search result:", linear_search(large_list, target))
    print("Binary search result:", binary_search(large_list, target))

    # Linear search may have to check almost every item.
    # Binary search keeps cutting the search area in half,
    # so it becomes much faster as the list gets larger.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty_list = []

    print("Empty list:")
    print("Linear search:", linear_search(empty_list, 10))
    print("Binary search:", binary_search(empty_list, 10))

    # Both searches return -1 because there is nothing to search.

    # Edge case 2: Single-element list
    single_list = [25]

    print("\nSingle-element list:")
    print("Searching for 25:")
    print("Linear search:", linear_search(single_list, 25))
    print("Binary search:", binary_search(single_list, 25))

    # Both searches find the only item at index 0.


if __name__ == "__main__":
    main()