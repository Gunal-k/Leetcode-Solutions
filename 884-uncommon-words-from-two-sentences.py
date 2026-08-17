class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = defaultdict(int)

        for word in (s1 + " " + s2).split():
            freq[word] += 1

        return [word for word, count in freq.items() if count == 1]
