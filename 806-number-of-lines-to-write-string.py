class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        cnt, pixels =1, 0
        for ch in s:
            val = widths[ord(ch)-ord('a')]
            pixels += val
            if pixels > 100:
                cnt +=1
                pixels = val
        return [cnt,pixels]
