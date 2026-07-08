# Traditional Binary Search - Looking up if number is in array:
# Time: O(logn)
# Space: O(1)
def binary_search(arr, target):
    n = len(arr) - 1
    L = 0
    R = n - 1

    while L <= R:
        M = L + ((R - L) // 2)
        if arr[M] == target:
            return True
        elif arr[M] > target:
            R = M - 1
        else:
            L = M + 1
    return False

# Condition based - Sử dụng với mảng True/False để tìm ra vị trí True đầu tiên
def binary_search_condition(arr):
    N = len(arr)
    L = 0
    R = N - 1
    while L < R:
        M = (L + R) // 2
        if arr[M]:
            R = M
        else:
            L = M + 1
    return L

if __name__ == '__main__':
    A = [-3, -1, 0, 1, 4, 7]

    # Linear Search O(n)
    if 9 in A:
        print(True)
    else:
        print(False)
    print(binary_search(A, -4))

    B = [False, False, False, False, True, True, True]
    print(binary_search_condition(B))