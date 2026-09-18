class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        i = 0
        sign = 1

        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        ans = 0

        while i < len(s) and s[i].isdigit():
            val = ans * 10 + int(s[i])
            if val >= 2**31:
                ret = (2**31) * sign
                return ret - 1 if sign > 0 else ret

            ans = val
            i += 1

        return ans * sign
