class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S, T = len(s), len(t)
        j = 0
        if s == '': return True
        if S > T: return False
        for i in range(T):
            if t[i] == s[j]:
                if j == S - 1:
                    return True
                j += 1
        return False

if __name__ == '__main__':
    solution = Solution()
    s = "abc"
    t = "ahcgdb"
    print(solution.isSubsequence(s, t))