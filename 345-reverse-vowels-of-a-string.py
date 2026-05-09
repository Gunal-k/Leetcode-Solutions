class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = "aeiouAEIOU"

        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] in vow:
                if s[r] in vow:
                    s[l], s[r] = s[r], s[l]
                    l += 1 
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
            
        return "".join(s)
