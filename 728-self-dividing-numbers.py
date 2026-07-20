class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        if left == 0:
            return ans
        def helper(num):
            act = num
            while num>0:
                val = num%10
                
                if val == 0 or act % val != 0:
                    return False
                
                num //=10
            return True
        
        while left <= right:
            if helper(left):
                ans.append(left)
            left +=1
        
        return ans
