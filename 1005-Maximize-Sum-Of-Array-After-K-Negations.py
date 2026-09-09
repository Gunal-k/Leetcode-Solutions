class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums.sort()
        i = 0

        while k > 0 and i < len(nums) and nums[i] < 0:
            nums[i] *= -1
            i += 1
            k -= 1

        if k % 2:
            i = min(range(len(nums)), key=lambda x: abs(nums[x]))
            nums[i] *= -1

        return sum(nums)
