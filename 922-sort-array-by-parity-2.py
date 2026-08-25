class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd = 1

        for i in range(0, n, 2):
            if nums[i] % 2 == 1:
                while nums[odd] % 2 == 1:
                    odd += 2
                nums[i], nums[odd] = nums[odd], nums[i]
        return nums
