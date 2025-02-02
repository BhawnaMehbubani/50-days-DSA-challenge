'''
Coding Exercise: Sorted Squared Array
Question
You are given an array of Integers in which each subsequent value is not less than the previous value. 
Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.
Remember
You can solve this question in multiple ways.
Think about the following -
1.What would be the brute force way of solving this question ? What would be the Time and Space complexity of this approach?
2.Is there a better way to solve this with a more optimum Time complexity than the Brute force way ? 
'''

def sorted_squared(array):
    #write code here.make sure to return desired array
    left, right = 0, len(array) - 1
    result = []

    while left <= right:
        left_square = array[left] ** 2
        right_square = array[right] ** 2

        if left_square > right_square:
            result.append(left_square)
            left += 1
        else:
            result.append(right_square)
            right -= 1

    # Since we appended in reverse order, reverse the result to get sorted order
    return result[::-1]

'''
The function uses a two-pointer approach to square the elements in a sorted array and build the result in one pass. It compares squares from both ends, appending the larger one to the result.

Time Complexity**: O(n) (single pass through the array)
Space Complexity: O(n) (storing the result array)

This is more efficient than the brute force approach, which would involve sorting the squared numbers. 
'''
