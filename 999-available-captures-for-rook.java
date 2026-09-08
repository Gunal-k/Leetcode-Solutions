class Solution {
    public int numRookCaptures(char[][] board) {
        int rookR = -1, rookC = -1;
        for (int r = 0; r < 8; r++)
            for (int c = 0; c < 8; c++)
                if (board[r][c] == 'R') {
                    rookR = r;
                    rookC = c;
                }

        int captures = 0;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int[] d : directions) {
            int nr = rookR + d[0], nc = rookC + d[1];
            while (nr >= 0 && nr < 8 && nc >= 0 && nc < 8) {
                if (board[nr][nc] == 'B') break;
                if (board[nr][nc] == 'p') {
                    captures++;
                    break;
                }
                nr += d[0];
                nc += d[1];
            }
        }
        return captures;
    }
}   
