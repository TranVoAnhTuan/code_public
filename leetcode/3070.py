class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pres = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                pres[i+1][j+1] = pres[i+1][j] + pres[i][j+1] - pres[i][j] + val
                ans += pres[i+1][j+1] <= k
        return ans
