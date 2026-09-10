"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # insert() puts the new value at the position we choose.
    # The items already in the list get moved over to make room for it.
    # Adding something near the beginning can take more work because
    # more items have to be moved. Adding it at the end is usually quicker.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check the index first so we don't try to remove something
    # that isn't actually in the list. This keeps the program from
    # giving an error when an invalid index is used.
    if index < 0 or index >= len(lst):
        return None

    # pop() removes the item and lets us save the value that was removed.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because the list is checked one item
    # at a time starting from the beginning.
    for i in range(len(lst)):
        if lst[i] == value:
            return i

    # If we go through the whole list without finding it, return -1.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    numbers = [10, 20, 30, 40]

    # Show what the list looks like before making changes.
    print("Original list:", numbers)

    # Add 5 to the beginning of the list.
    # The other numbers move over to make room.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Add 25 somewhere in the middle of the list.
    # The numbers after it are moved over.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle:", numbers)


    # Add 50 to the end of the list.
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end:", numbers)



    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Remove the first item in the list.
    # The removed value is saved so we can print it.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Remove an item from the middle of the list.
    removed = delete_at(numbers, 2)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Remove the last item in the list.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # Look for a number that is already in the list.
    result = search_value(numbers, 30)
    print("Searching for 30. Index:", result)

    # Look for a number that is not in the list.
    # The result should be -1.
    result = search_value(numbers, 100)
    print("Searching for 100. Index:", result)



    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Try deleting an index that does not exist.
    # None is returned instead of causing the program to crash.
    result = delete_at(numbers, 100)
    print("Delete using invalid index:", result)

    # Try searching for a number that is not in the list.
    # The function should return -1.
    result = search_value(numbers, 999)
    print("Search for missing value:", result)

    # Test inserting a value into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 42)
    print("Insert into empty list:", empty_list)



if __name__ == "__main__":
    main()