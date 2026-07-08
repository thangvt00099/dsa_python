import heapq

# Heap Sort
# Time: O(n logn), Space: O(n)
def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list

if __name__ == '__main__':
    # Build Min Heap (Heapify)
    # Time : O(n), Space: O(1)
    A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

    # Sử dụng heapify để sắp xếp lại cây
    heapq.heapify(A)

    # Heap push (Insert Element)
    # Time: O(log n)
    heapq.heappush(A, 4)

    # Peak at Min (search min) - view not remove as pop
    # Time: O(1)
    print(A[0])

    # Heap pop (Extract min)
    # Time: O(log n)
    minn = heapq.heappop(A)
    print(A)
    print(minn)

    # Heap push pop
    # Time: O(log n)
    heapq.heappushpop(A, 99)
    print(A)

    new_arr = heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(new_arr)
