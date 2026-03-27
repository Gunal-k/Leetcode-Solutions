class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = len(nums)
        if target >max(nums):
            return a
        for i in range(a):
            if nums[i]< target:
                continue
            else:
                break
        return i 