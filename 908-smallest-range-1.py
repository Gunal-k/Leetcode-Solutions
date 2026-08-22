class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mini = maxi = nums[0]

        for num in nums:
            mini = min(mini,num)
            maxi = max(maxi,num)
        
        return max(0,maxi-mini-2*k)
