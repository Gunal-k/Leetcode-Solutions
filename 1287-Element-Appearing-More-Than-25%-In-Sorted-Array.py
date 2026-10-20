class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        lim = len(arr)//4
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1

            if freq[num] > lim:
                    return num
