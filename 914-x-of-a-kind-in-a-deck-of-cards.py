class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck:
            return False
        counts = Counter(deck).values()
        return reduce(gcd, counts) >= 2
