class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ops in operations:
            if ops == 'C':
                stk.pop()
            elif ops == 'D':
                stk.append(2 * stk[-1])
            elif ops == '+':
                stk.append(stk[-1]+stk[-2])
            else:
                stk.append(int(ops))
        return sum(stk)
