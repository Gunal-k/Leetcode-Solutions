class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            j = 0
            n = len(grid[i])
            if grid[i][n-1] >= 0:
                continue
            while j < n and grid[i][j] >= 0:
                pass
                j+=1
            cnt += n - j
        return cnt
