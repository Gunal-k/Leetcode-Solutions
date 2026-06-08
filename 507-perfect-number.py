class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Perfect numbers must be positive and greater than 1
        if num <= 1:
            return False
        
        # 1 is always a proper divisor
        divisor_sum = 1
        
        # Iterate up to the square root of num
        upper_limit = int(num ** 0.5)
        for i in range(2, upper_limit + 1):
            if num % i == 0:
                divisor_sum += i
                # Avoid double counting if divisors are identical (e.g., 6*6 = 36)
                if i != num // i:
                    divisor_sum += num // i
                    
        return divisor_sum == num
