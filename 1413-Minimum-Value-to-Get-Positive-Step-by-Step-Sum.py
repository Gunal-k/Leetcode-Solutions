class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefix = 0
        min_prefix = 0

        for num in nums:
            prefix += num
            min_prefix = min(min_prefix, prefix)

        return 1 - min_prefix
