class Solution:
    arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transform = set()
        for word in words:
            form = "".join(self.arr[ord(ch) - ord('a')] for ch in word)
            transform.add(form)
        return len(transform)
