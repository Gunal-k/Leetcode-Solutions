class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = "aeiouAEIOU"
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            words[i] = word + "a" * (i+1)

        return " ".join(words)
