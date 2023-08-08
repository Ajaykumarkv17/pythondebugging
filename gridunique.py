class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countPaths(i, j, n, m):
            if i == (n - 1) and j == (m - 1):
                return 1
            if i >= n or j >= m:
                return 0
            else:
                return countPaths(i + 1, j, n, m) + countPaths(i, j + 1, n, m)


        return countPaths(0, 0, m, n)




if __name__ == "__main__":
    obj = Solution()
    totalCount = obj.uniquePaths(3, 7)
    print("The total number of Unique Paths are ", totalCount)