class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # i = 1
        # while i**2 <= num:
        #     if i**2 == num:
        #         return True
        #     i+=1
        # return False

        l, r = 1, num
        while l<=r:
            mid = (l+r) //2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False