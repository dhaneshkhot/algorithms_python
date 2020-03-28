class DiagonalDifference:
    def get_diagonal_difference(self, matrix):
        diagonal_sum_1 = 0
        diagonal_sum_2 = 0

        m_len = len(matrix)

        for i in range(m_len):
            for j in range(m_len):
                if i == j:
                    diagonal_sum_1 = diagonal_sum_1 + matrix[i][j]
                if (i+j) == m_len-1:
                    diagonal_sum_2 = diagonal_sum_2 + matrix[i][j]

        return abs(diagonal_sum_1 - diagonal_sum_2)
