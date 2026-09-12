class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        current_val = 0
        for num in nums:
            current_val = (current_val * 2 + num) % 5
            ans.append(current_val == 0)
        return ans   
