class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mincr , mdecr = True, True
        for i in range(1,len(nums)):
            if not (nums[i-1] <= nums[i]):
                mincr = False
            if not (nums[i-1] >= nums[i]):
                mdecr = False
        return mincr or mdecr
