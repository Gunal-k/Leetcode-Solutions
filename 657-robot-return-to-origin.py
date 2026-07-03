class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h = v = 0
        for chr in moves:
            if chr == 'R':
                h+=1
            elif chr == 'U':
                v+=1
            elif chr == 'L':
                h-=1
            else:
                v-=1
        return h == 0 and v == 0
