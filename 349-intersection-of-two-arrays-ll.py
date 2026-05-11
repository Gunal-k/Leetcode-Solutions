class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        visited = {}

        for num in nums1:
            visited[num] = visited.get(num, 0) + 1
        for num in nums2:
            if num in visited and visited[num] > 0:
                visited[num] -= 1
                ans.append(num)
        return ans