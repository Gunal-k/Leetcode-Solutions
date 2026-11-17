class Solution:
    def reformat(self, s: str) -> str:
        digits = []
        letters = []

        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)

        if abs(len(digits) - len(letters)) > 1:
            return ""

        longer, shorter = letters, digits

        if len(digits) > len(letters):
            longer, shorter = digits, letters

        result = [""] * len(s)
        result[::2] = longer
        result[1::2] = shorter

        return "".join(result)
