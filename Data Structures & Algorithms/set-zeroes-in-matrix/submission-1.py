class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zeros = set()
        col_zeros = set()

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)

        for i in range(len(matrix)):
            if i in row_zeros:
                matrix[i] = [0 for _ in matrix[i]]

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):  
                if j in col_zeros:
                    matrix[i][j] = 0


