class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt = ans = 1
        i = 0
        while i < len(nums) - 1:
            if nums[i+1] <= nums[i]:
                ans = max(ans,cnt)
                cnt = 0
            cnt+=1
            i+=1
        return max(ans,cnt)
