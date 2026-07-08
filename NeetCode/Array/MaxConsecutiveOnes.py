class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        max_cnt, j = 0, 0
        for i in range(n):
            if nums[i] == 1:
                j += 1
            else:
                j = 0
            max_cnt = max(max_cnt, j)

        return max_cnt

if __name__ == '__main__':
    solution = Solution()
    # nums = [1,1,0,1,1,1]
    nums = [1,0,1,1,0,1]
    print(solution.findMaxConsecutiveOnes(nums))