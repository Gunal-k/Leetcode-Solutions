class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        freq = {}
        for char in magazine:
            freq[char] = freq.get(char,0) + 1
        for char in ransomNote:
            freq[char] = freq.get(char,0) - 1
            if(freq[char] < 0):
                return False
        return True