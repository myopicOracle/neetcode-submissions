class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        # 4 boundaries
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while (left < right) and (top < bottom):
        # while len(res) <= len(matrix) * len(matrix[0]):

            # traverse top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # traverse right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # guard single rol/col
            if not ((left < right) and (top < bottom)):
                break

            # traverse bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # traverse left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res