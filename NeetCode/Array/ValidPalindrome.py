class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(c.lower() for c in s if c.isalnum())
        return t == t[::-1]

if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    solution = Solution()
    print(solution.isPalindrome(s))