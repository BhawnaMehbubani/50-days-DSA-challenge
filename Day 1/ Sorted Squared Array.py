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
    