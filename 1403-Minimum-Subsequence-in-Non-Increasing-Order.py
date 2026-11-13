class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        nums.sort(reverse=True)

        selected_sum = 0
        result = []

        for num in nums:
            result.append(num)
            selected_sum += num

            if selected_sum > total - selected_sum:
                break

        return result
