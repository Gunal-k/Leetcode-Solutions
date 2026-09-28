class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for char in address:
            if char.isdigit():
                ans += char
            else:
                ans += "[.]"

        return ans
