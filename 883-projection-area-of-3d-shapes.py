class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum(v>0 for row in grid for v in row)
        front = sum(map(max,grid))
        side = sum(map(max,zip(*grid)))
        return top + front + side
