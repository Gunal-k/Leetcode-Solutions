class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

        result = [""] * len(score)
        
        for rank, (original_index, _) in enumerate(sorted_scores):
            if rank == 0:
                result[original_index] = "Gold Medal"
            elif rank == 1:
                result[original_index] = "Silver Medal"
            elif rank == 2:
                result[original_index] = "Bronze Medal"
            else:
                result[original_index] = str(rank + 1)

        return result