class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        copy = [row[:] for row in matrix]

        for i, row in enumerate(matrix):
            k = len(matrix) - 1

            for j, col in enumerate(row):
                matrix[i][j] = copy[k][i]
                k -= 1

        #return matrix



# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]        

# matrix = [
#     [0][0,1,2],
#     [1][0,1,2],
#     [2][0,1,2]
# ]       

# matrix = [
#     [0][0], [0][1], [0][2], 
#     [1][0], [1][1], [1][2], 
#     [2][0], [2][1], [2][2], 
# ]   

# # rows and columns swapped





