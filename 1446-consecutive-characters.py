class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        maxCount = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 1

        return maxCount
