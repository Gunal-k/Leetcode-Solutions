class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, digit_sum = 1, 0
        while n > 0:
            n, digit = divmod(n, 10)
            product *= digit
            digit_sum += digit
        return product - digit_sum   
