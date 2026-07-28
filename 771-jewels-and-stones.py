class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = defaultdict(int)
        for char in stones:
            freq[char] +=1
        ans = 0
        for char in set(jewels):
            if char in stones:
                ans+=freq[char]
        return ans
