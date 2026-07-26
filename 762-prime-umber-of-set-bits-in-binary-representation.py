class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n == 1:
                return False
            if n == 2:
                return True
            if n%2 == 0:
                return False
            for i in range(3,int(n**0.5 + 1),2):
                if n % i == 0:
                    return False
            return True
        ans = 0
        for i in range(left,right+1):
            val = bin(i).count("1")
            if is_prime(val):
                ans+=1
        return ans


#optimized

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5 + 1),2):
        if n % i == 0:
            return False
    return True

pref = [0]

for i in range(1,10000001):
    val = bin(i).count("1")
    if is_prime(val):
        pref.append(pref[i-1]+1)
    else:
        pref.append(pref[-1])

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        return pref[right]-pref[left-1]
