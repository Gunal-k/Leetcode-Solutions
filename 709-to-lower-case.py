class Solution:
    def toLowerCase(self, s: str) -> str:

        ans = []

        for ch in s:

            if 'A' <= ch <= 'Z':
                ans.append(chr(ord(ch) + 32))
            else:
                ans.append(ch)

        return "".join(ans)
        
        #return s.lower()
