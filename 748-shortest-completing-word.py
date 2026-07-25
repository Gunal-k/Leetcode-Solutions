class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        freq = [0]*26
        
        for char in licensePlate.lower():
            if char.isalpha():
                freq[ord(char)-ord('a')] += 1

        ans = ""
        
        for word in words:

            f = [0]*26

            for char in word:
                if char.isalpha():
                    f[ord(char)-ord('a')] += 1
            
            valid = True

            for i in range(26):
                if f[i] < freq[i]:
                    valid = False
                    break
            
            if valid:
                if ans == "" or len(word) < len(ans):
                    ans = word
        return ans
