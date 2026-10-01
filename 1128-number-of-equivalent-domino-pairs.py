class Solution:
    def numEquivDominoPairs(self, dominoes):
        count = {}
        ans = 0

        for a, b in dominoes:
            # Make [1,2] and [2,1] the same
            a, b = min(a, b), max(a, b)

            key = (a, b)

            # Every previous equivalent domino makes one new pair
            ans += count.get(key, 0)

            # Increase frequency
            count[key] = count.get(key, 0) + 1

        return ans
