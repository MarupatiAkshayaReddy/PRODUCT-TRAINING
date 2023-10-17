def quick_sort(arr):
    if len(arr) <= 1:
        return arr
        
    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
arr = list(map(int,input().split()))
print(arr)
result = quick_sort(arr)
print(result)