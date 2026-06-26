class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {}

        for i, restaurant in enumerate(list1):
            mp[restaurant] = i

        ans = []
        minSum = float("inf")

        for j, restaurant in enumerate(list2):
            if restaurant in mp:
                curr = mp[restaurant] + j

                if curr < minSum:
                    minSum = curr
                    ans = [restaurant]
                elif curr == minSum:
                    ans.append(restaurant)

        return ans
