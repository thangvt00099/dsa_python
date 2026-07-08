class Solution:
    # C1 - Dict
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    # C2 - Sorted
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    s = "racecar"
    t = "carrace"
    solution = Solution()
    print(solution.isAnagram2(s, t))