from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        banned = set(banned)

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.lower().split()

        count = Counter()

        for word in words:
            if word not in banned:
                count[word] += 1

        return max(count, key=count.get)
