class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for i in range(1,rowIndex+1):
            row = []
            for j in range(i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    val = triangle[0][j-1] + triangle[0][j]
                    row.append(val)
            triangle[0] = row
        return triangle[0]