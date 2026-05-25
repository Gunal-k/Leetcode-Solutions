class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        ans = 0
        while l<=r:
            mid = (l+r)//2
            coins = (mid*(mid+1))//2
            if coins <=n:
                ans = max(ans,mid)
                l = mid+1
            else:
                r = mid-1
        return ans