class Solution:
    # C1 Sorted - O(n)
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums_sort = sorted(nums)
        for i in range(1, len(nums_sort)):
            if nums_sort[i] == nums_sort[i - 1]:
                return True
        return False

    # C2 - Set - O(n)
    def hasDuplicate2(self, nums: list[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

    # C3 - Length Set - O(n)
    def hasDuplicate3(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

if __name__ == '__main__':
    nums = [1, 2, 3, 3]
    solution = Solution()
    print(solution.hasDuplicate3(nums))