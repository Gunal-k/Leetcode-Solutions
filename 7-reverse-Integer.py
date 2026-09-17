class Solution:
    def reverse(self, x: int) -> int:
        s = 1 if x > 0 else -1
        ans = 0
        x = abs(x)

        while x:
            a = x % 10
            b = (ans * 10) + a

            if b <= (2**31) - 1:
                ans = b
            else:
                return 0

            x //= 10

        return ans * s
