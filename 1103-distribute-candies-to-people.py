class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        i = 1
        j = 0
        ans = [0] * num_people
        while candies > 0:
            ad = min(i, candies)
            ans[j] += ad
            candies -= ad
            j += 1
            if j == num_people:
                j = 0
            i += 1

        return ans
