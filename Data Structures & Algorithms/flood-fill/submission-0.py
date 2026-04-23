class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # If the starting pixel already has the target color, nothing to do.
        if image[sr][sc] == color:
            return image

        # Dimensions of the image
        nrows, ncols = len(image), len(image[0])

        # DFS to fill connected region of the original color
        # r, c: current coordinates
        # orig: original color we are replacing
        def dfs(r, c, orig):
            # Boundary and color-check: stop if out of bounds or color mismatch
            if not (0 <= r < nrows) or not (0 <= c < ncols) or image[r][c] != orig:
                return

            # Paint current pixel with the target color
            image[r][c] = color

            # Recurse for all 4 neighbors
            dfs(r + 1, c, orig)  # down
            dfs(r - 1, c, orig)  # up
            dfs(r, c + 1, orig)  # right
            dfs(r, c - 1, orig)  # left

        # Start DFS from the starting pixel, capturing its original color
        dfs(sr, sc, image[sr][sc])

        # Return the modified image
        return image