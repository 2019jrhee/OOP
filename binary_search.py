# binary search for a number
def binary_search (arr, n):
    #find the middle of the array
    mid = arr[len(arr)//2]
    print (mid)


#1 what if the search number isn't in the array?
#2 what if the number is found?
#3 conditional for loawer half & upper half based on our find input

    #if the number is the middle number, then return true
    if n == mid: return True

    # if the number is greater than the middle number, then return one higher
    if n > mid: return binary_search(arr[len(arr)//2+1:], n)

    #if the number is less than the middle number, then return one smaller
    if n < mid: return binary_search(arr[:len(arr)//2], n)

arr = [1,2,3,4,5,6,7,8,9]
binary_search (arr,6)
