# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.


While working on this assignment, I learned how stacks and queues work in Python and how they are used to organize data.
I learned that a stack uses LIFO, which means the last item added is the first one removed. A queue uses FIFO, meaning
the first item added is the first one removed. I also got more practice using Python lists and the deque data structure.

One challenge I had was getting the queue to work correctly, especially when using popleft() and testing an empty queue. 
I also ran into an error when front() tried to access an item from an empty queue. I fixed this by adding a check to see
if the queue was empty before trying to remove or view an item.

Stacks and queues are useful in real-world situations because they handle information in different ways. A stack could
be used for browser history or undoing an action, where the most recent action is handled first. A queue could be used 
for a printer or customer service line, where the first person or request in line should be handled first.