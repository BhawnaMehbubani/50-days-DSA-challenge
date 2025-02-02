'''
Coding Exercise: Monotonic Array
Question
An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing. 
An array is monotone decreasing if all  its elements from left to right are non-increasing. 
Given an integer array return true if the given array is monotonic, or false otherwise.
'''
def monotonic_array(array):
    #write code here
    n=len(array)
    if n==0: return True
    if n==1: return True
    first=array[0]
    last=array[n-1]
    if first>last:
        for k in range(n-1):
            #MD or not monotonic
            if array[k]<array[k+1]:
                return False
    elif first == last:
        for k in range(n-1):
            #MD if all values are same
            if array[k]!=array[k+1]:
                return False
    else:
        for k in range(n-1):
            #MI or not monotonic
            if array[k]>array[k+1]:
                return False
    return True
        


print(monotonic_array([1]))
