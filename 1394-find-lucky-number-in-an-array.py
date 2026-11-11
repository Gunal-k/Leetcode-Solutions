class Solution:
    def findLucky(self, arr: list[int]) -> int:
        ans = -1
        freq = Counter(arr)
        for key,val in freq.items():
            if key == val:
                ans = max(ans, val)

        return ans
