class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)

        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(solution.removeElement(nums, val))