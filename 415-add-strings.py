class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        i = len(num1) -1
        j = len(num2) -1
        carry = 0
        while i>=0 or j>=0 or carry !=0:
            digit1 = int(num1[i]) if i>=0 else 0
            digit2 = int(num2[j]) if j>=0 else 0

            res = digit1 + digit2 + carry
            carry = res // 10

            ans.append(res % 10)
            i-=1
            j-=1
        return "".join(map(str,ans[::-1]))