class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for word in words:
            fchar = word[0].lower()
            if fchar in row1:
                target = row1
            elif fchar in row2:
                target = row2
            else:
                target = row3 
            
            if set(word.lower()) <= target:
                ans.append(word)
        return ans