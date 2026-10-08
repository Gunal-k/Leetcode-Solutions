class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        arr = Counter(text)
        ans = float("inf")

        for char in "balloon":
            val = arr[char]
            if char in "lo":
                val //= 2
            ans = min(val, ans)
        return ans
