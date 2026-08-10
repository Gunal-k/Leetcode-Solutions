class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)

        dif = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                dif.append(i)
        
        if len(dif) != 2:
            return False
        
        i, j = dif
        return s[i] == goal[j] and goal[i] == s[j]
