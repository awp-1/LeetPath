class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]*i for i in range(1,rowIndex+2)]
        if rowIndex >= 2:
            for i in range(2,rowIndex+1):
                for j in range(1,i):
                    print(pascal)
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal[rowIndex]