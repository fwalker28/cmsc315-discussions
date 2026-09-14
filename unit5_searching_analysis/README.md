# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

I learned how linear and binary searches work and how to use them in Python. I also learned that binary search needs
a sorted list and can find things faster by cutting the search area in half.

One challenge I had was understanding how binary search keeps changing the search area. I worked through it by
looking at each step and seeing how the middle value determines which half of the list to search next. Testing 
different values also helped me understand it better.

Linear search is useful for smaller or unsorted lists because it can search through the list without needing it
to be sorted. Binary search is better for larger sorted lists because it is much faster. The tradeoff is that binary
search requires the data to be sorted first, while linear search does not.