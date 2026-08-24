"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        self.stack = []
        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.stack.append(value) #new values are added top of stack, that supported LIF0
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if not self.stack:
            return None
        return self.stack.pop()
        pass

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if not self.stack:
            return None
        return self.stack[-1] #peek looks at top value without removing it
        pass

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        if not self.stack:
            return None
        return len(self.stack) == 0
        pass


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.queue.append(value) #new values go to the back
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if not self.queue:
            return None
        return self.queue.popleft()
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0] #front shows the first value without removing it
        pass

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0
        pass


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    stack = Stack()

    stack.push('1')
    stack.push('2')
    stack.push('3')
    stack.push('4')

    print("\n=== STACK DEMO ===")
    print("added 1,2,3,4 to the stack")

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print("Test Pop from empty stack:", stack.pop())
    print("Test peek from empty stack:", stack.peek())

    single_stack = Stack()
    single_stack.push("One")
    print("Single Item Stack:", single_stack.peek())
    single_stack.pop()

    print("Is single-item stack empty?", single_stack.is_empty())


# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    queue = Queue()

    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')
    queue.enqueue('4')

    print("\n=== QUEUE DEMO ===")
    print("added 1,2,3,4 to the queue")

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print("Dequeue from empty queue:", queue.dequeue())
    print("Front of empty queue:", queue.front())

    single_queue = Queue()
    single_queue.enqueue("One")
    print("Single-item queue:", single_queue.front())
    single_queue.dequeue()
    print("Is single-item queue empty?", single_queue.is_empty())
if __name__ == "__main__":
    main()
