class Solution(object):
    def floodFill(self, image, sr, sc, color):
        startColor=image[sr][sc]
        if startColor == color:
            return image
        def dfs(sr, sc):
            if sr<0 or sr >= len(image) or sc<0 or sc >= len(image[0]) or image[sr][sc] != startColor:
                return
            image[sr][sc] = color
            for i, j in [[-1, 0], [1,0], [0,-1], [0,1]]:
                dfs(sr+i, sc+j)

        dfs(sr, sc)
        return image