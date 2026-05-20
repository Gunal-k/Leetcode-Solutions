class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        map = "0123456789abcdef"
        res = ""

        while num and len(res) < 8:
            res = map[num&15] + res
            num = num >> 4
        return res