class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []
        word = 1

        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            if word == 2:
                s.append(word2[b])
                b += 1
                word = 1

        while a < A:
            s.append(word1[a])
            a += 1
        while b < B:
            s.append(word2[b])
            b += 1

        return ''.join(s)

if __name__ == '__main__':
    solution = Solution()
    # word1 = "abc"
    # word2 = "pqr"
    # word1 = "ab"
    # word2 = "pqrs"
    word1 = "abcd"
    word2 = "pq"
    print(solution.mergeAlternately(word1, word2))