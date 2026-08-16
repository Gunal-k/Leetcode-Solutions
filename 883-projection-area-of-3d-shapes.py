class Solution {
    public int projectionArea(int[][] grid) {
        int x = 0;
        int y = 0;
        int z = 0;

        int n = grid.length;

        for (int i = 0; i < n; i++) {
            int rowMax = 0;
            int colMax = 0;

            for (int j = 0; j < n; j++) {
                rowMax = Math.max(rowMax, grid[i][j]);
                colMax = Math.max(colMax, grid[j][i]);

                if (grid[i][j] > 0)
                    z++;
            }

            x += rowMax;
            y += colMax;
        }

        return x + y + z;
    }
}
