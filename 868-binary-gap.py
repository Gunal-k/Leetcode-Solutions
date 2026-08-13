class Solution:
    def binaryGap(self, n: int) -> int:
        val = bin(n)[2:]
        index = -1
        ans = 0
        for i, num in enumerate(val):
            if num == '1':
                if index != -1:
                    ans = max(i - index,ans)
                index = i
        return ans
