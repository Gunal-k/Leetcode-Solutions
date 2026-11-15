class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        initial = -1
        for i, j in enumerate(nums):
            if j == 1:
                if initial != -1 and i - initial <= k:
                    return False

                initial = i

        return True
