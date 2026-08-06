class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        ans = []
        start = 0

        for i in range(1, len(s)):

            if s[i] != s[start]:

                if i - start >= 3:
                    ans.append([start, i - 1])

                start = i

        if len(s) - start >= 3:
            ans.append([start, len(s) - 1])

        return ans
