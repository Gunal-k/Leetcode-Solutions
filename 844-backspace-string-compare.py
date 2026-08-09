class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            s = []
            for ch in string:
                if ch != '#':
                    s.append(ch)
                else:
                    if s:
                        s.pop()
            return "".join(s)
        return build(s) == build(t)
