#My code
class Solution:
    def isPalindrome(self, x: int) -> bool:
        val = x
        rev = 0
        while val>0:
            temp = val % 10
            val = val//10
            rev = rev * 10 + temp
        return x == rev

#Optimal code
class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = str(x)
        return b == b[::-1]