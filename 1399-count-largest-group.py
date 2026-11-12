class Solution:
    def countLargestGroup(self, n: int) -> int:

        freq = {}

        for num in range(1, n + 1):

            digit_sum = 0
            temp = num

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            freq[digit_sum] = freq.get(digit_sum, 0) + 1

        max_size = max(freq.values())

        return sum(1 for count in freq.values()
                   if count == max_size)
