class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()

        for i, row in enumerate(matrix):

            for j, num in enumerate(row): 

                if num == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)       


        for r in zero_rows:
            matrix[r] = [0 for x in matrix[r]]


        for i, row in enumerate(matrix):

            for j, num in enumerate(row): 

                if j in zero_cols:
                    matrix[i][j] = 0



    
# def setZeroes(self, matrix: List[List[int]]) -> None:

#     self.setRowZero(matrix)

#     matrix.reverse()
#     self.setRowZero(matrix)

#     matrix.reverse()


# def setRowZero(self, matrix: List[List[int]]) -> None:
#     for i, row in enumerate(matrix):
#         if 0 in row:
#             matrix[i] = [0 for x in matrix[i]]


# Brute 1: incomplete
# row_length = len(matrix[0])
# col_length = len(matrix)

# zero_rows = set()
# zero_cols = set()

# for i, row in enumerate(matrix):

#     for j, num in enumerate(row): 

#         if num == 0:
#             zero_rows.add(i)
#             zero_cols.add(j)       


# for r in zero_rows:
#     matrix[r] = [0 for x in matrix[r]]


# for c in zero_cols:
#     ...


