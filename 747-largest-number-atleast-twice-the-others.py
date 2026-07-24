class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        largest = second = -1
        index = 0

        for i, num in enumerate(nums):

            if num > largest:
                second = largest
                largest = num
                index = i

            elif num > second:
                second = num

        return index if largest >= 2 * second else -1
