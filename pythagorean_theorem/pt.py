
def pt_naive(arr, size):
    for x in range(size):
        for y in range(x+1, size):
            for z in range(x+2, size):
                a = arr[x] * arr[x]
                b = arr[y] * arr[y]
                c = arr[z] * arr[z]
                if(a == b + c or b == a + c or c == b + a):
                    return 1
    return 0

def pt_sort(arr, size):
    for i in range(size):
        arr[i] = arr[i] * arr[i]

    arr.sort()
    
    for i in range(size-1, 1, -1):
        left = 0
        right = i - 1

        while(left < right):
            if (arr[left] + arr[right] == arr[i]):
                return 1
            else:
                if (arr[left] + arr[right] < arr[i]):
                    left += 1
                else:
                    right -= 1
    return 0

arr = [3, 1, 4, 6, 5]
print('naive', pt_naive(arr, len(arr)))

arr = [3, 1, 4, 6, 5]
print('sort', pt_sort(arr, len(arr)))

