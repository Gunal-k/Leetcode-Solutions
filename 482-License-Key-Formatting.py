class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ms = s.replace("-","").upper()
        i = len(ms)%k or k
        j = 0
        ans = []
        while i <= len(ms):
            ans.append(ms[j:i])
            j = i
            i += k 
        return "-".join(ans)