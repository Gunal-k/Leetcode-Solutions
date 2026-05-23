class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq1 = {}
        for char in words[0]:
            freq1[char] = freq1.get(char,0) + 1
        for i in range(1,len(words)):
            freq2 = {}
            for char in words[i]:
                freq2[char] = freq2.get(char,0) + 1
            for char in freq1:
                if char in freq2:
                    freq1[char] = min(freq1[char], freq2[char])
                else:
                    freq1[char] = 0

        ans = []
        for x,num in freq1.items():
            for i in range(num):
                ans.append(x)

        return ans