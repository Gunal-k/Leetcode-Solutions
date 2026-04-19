class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        for num in set(nums):
            if nums.count(num) > n:
                return num