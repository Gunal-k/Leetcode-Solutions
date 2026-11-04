class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        count_map = {}

        for i, num in enumerate(sorted_nums):
            if num not in count_map:
                count_map[num] = i

        result = []

        for num in nums:
            result.append(count_map[num])

        return result
