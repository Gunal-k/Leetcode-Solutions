class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_upper = 0
        count = 0

        for i in range(len(word)):
            if word[i].isupper():
                count+=1
                if i == 0:
                    first_upper = 1
                else:
                    first_upper = 2
        
        if count == 0:
            return True
        elif count == len(word):
            return True
        elif first_upper == 1:
            return True
        else:
            return False