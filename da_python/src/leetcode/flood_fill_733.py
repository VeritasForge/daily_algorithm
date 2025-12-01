# https://leetcode.com/problems/flood-fill/
# 733. Flood Fill
#
# An image is represented by an m x n integer grid `image` where image[i][j]
# represents the pixel value of the image. You are also given three integers
# sr, sc, and color. You should perform a flood fill on the image starting
# from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.
#
# Constraints:
# - m == image.length
# - n == image[i].length
# - 1 <= m, n <= 50
# - 0 <= image[i][j], color < 2^16
# - 0 <= sr < m
# - 0 <= sc < n


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    if image[sr][sc] != color:  # early return
        _dfs(image, sr, sc, color, image[sr][sc])

    return image


def _dfs(
    image: list[list[int]],
    sr: int,
    sc: int,
    color: int,
    origin_color: int,
):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
        return

    if image[sr][sc] != origin_color:
        return

    image[sr][sc] = color

    _dfs(image, sr - 1, sc, color, origin_color)
    _dfs(image, sr + 1, sc, color, origin_color)
    _dfs(image, sr, sc - 1, color, origin_color)
    _dfs(image, sr, sc + 1, color, origin_color)
