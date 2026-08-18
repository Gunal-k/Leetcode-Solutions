class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob = set(bobSizes)

        for x in aliceSizes:
            y = x - diff

            if y in bob:
                return [x, y]
