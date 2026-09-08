class Solution:
    def numRookCaptures(self, board):
        # Find the rook
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_r, rook_c = r, c

        captures = 0

        # Four directions: up, down, left, right
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:
            nr, nc = rook_r + dr, rook_c + dc

            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'B':
                    break

                if board[nr][nc] == 'p':
                    captures += 1
                    break

                nr += dr
                nc += dc

        return captures
