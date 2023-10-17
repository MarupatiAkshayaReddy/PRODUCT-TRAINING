def bs(arr, target):
    left, right = 0, len(arr) - 1
    floor=-1
    ceil=-1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return arr[mid], arr[mid]

        elif arr[mid] < target:
            floor = arr[mid]
            left = mid + 1

        else:
            ceil = arr[mid]
            right = mid - 1

    return floor, ceil

# Example usage:
arr = list(map(int,input().split()))
target=int(input())

ans = bs(arr, target)
print(ans[0],",",ans[1])
