class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available = Counter(chars)
        total = 0

        for word in words:
            required = Counter(word)

            if all(required[c] <= available[c] for c in required):
                total += len(word)

        return total
