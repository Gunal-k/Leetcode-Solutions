class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        visited = set(nums1)
        for num in nums2:
            if num in visited:
                ans.add(num)
        return list(ans)