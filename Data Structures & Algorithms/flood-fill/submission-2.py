class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def fillFromPoint(r: int, c: int, old_color: int, new_color: int) -> None:
            # at every point r, c
            # color (r, c ) with new color
            # we find all direct neighbors (no diagonal)
            # for each that has same color as ORIGINAL (r, c) -- we 
            if new_color == old_color: return

            if image[r][c] != old_color:
                return

            image[r][c] = new_color
            dirs = [
                (-1, 0), # above
                (0, -1), # left 
                (0, 1), # right
                (1, 0) # below
            ]
            for d in dirs:
                new_r, new_c = r + d[0], c + d[1]
                if new_r >= len(image) or new_r < 0 or new_c >= len(image[0]) or new_c < 0: continue
                if image[new_r][new_c] == old_color:
                    fillFromPoint(new_r, new_c, old_color, new_color)

        fillFromPoint(sr, sc, image[sr][sc], color)
        return image