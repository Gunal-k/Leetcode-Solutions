class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] +=1
        for i , ch in enumerate(s):
            if freq[ord(ch) - ord('a')] == 1:
                return i
        return -1