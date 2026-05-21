class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char,0) + 1

        ans = 0
        odd = False
        for num in freq.values():
                if num % 2 == 0:
                    ans += num
                else:
                    ans += num - 1
                    odd = True
                 
        return ans + 1 if odd else ans

        # seen = set()
        # for i in range (len(s)):
        #     if s[i] in seen:
        #         seen.remove(s[i])
        #     else:
        #         seen.add(s[i])
        # return len(s)-len(seen)+bool(seen)