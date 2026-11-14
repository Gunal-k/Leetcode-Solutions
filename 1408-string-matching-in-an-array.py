class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        # Sort words from shortest to longest
        words.sort(key=len)
        res = []
        n = len(words)
        
        for i in range(n):
            # Only check words that are at least as long as words[i]
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
                    
        return res
