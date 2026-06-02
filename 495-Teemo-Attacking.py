class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        for i in range(len(timeSeries)-1):
            gap = timeSeries[i+1] - timeSeries[i]
            count+=min(gap,duration)
            
        return count + duration