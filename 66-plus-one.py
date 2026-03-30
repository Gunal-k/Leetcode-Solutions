class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(map(str,digits))
        total = int(s) + 1

        return [int(d) for d in str(total)]