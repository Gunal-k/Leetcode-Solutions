from typing import List
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1 = self.convertToMinutes(event1[0])
        end1 = self.convertToMinutes(event1[1])
        start2 = self.convertToMinutes(event2[0])
        end2 = self.convertToMinutes(event2[1])
        return start1 <= end2 and start2 <= end1

    def convertToMinutes(self, h : str) -> int:
        h, m = map(int,h.split(":"))
        return h*60 + m

        # start1, end1 = event1
        # start2, end2 = event2
        # return start1 <= end2 and start2 <= end1