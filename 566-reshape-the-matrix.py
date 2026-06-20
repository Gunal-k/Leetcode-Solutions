class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        arr = [num for row in mat for num in row]

        ans = []

        for i in range(0, len(arr), c):
            ans.append(arr[i:i + c])

        return ans
