class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 - pix for pix in pix_arr[::-1]] for pix_arr in image]
