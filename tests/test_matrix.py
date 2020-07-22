# # #need inverse by minors, determinant, and recursive_determinant
import sys
sys.path.append('src')
# #add
from matrix import Matrix
# a = Matrix(elements = [[1,3,5],[7,9,11],[13,15,17]])
# b = Matrix(elements = [[0,2,4],[6,8,10],[12,14,16]])
# (a+b).show()
# #subtract
# (a-b).show()
# #scale
# (a*3).show()
# #matrix multiplication
# (a @ b).show()
# #Transpose
# (a.transpose()).show()
# square_identity = Matrix(elements = [[1,0,3],[2,1,0],[3,3,3]])
# tall_identity = Matrix(elements = [[1,2],[3,4],[5,6]])
# wide_identity = Matrix(elements = [[4,5,9],[1,-2,3]])
# square_non_identity = Matrix(elements = [[1,2,3],[4,5,6],[7,8,9]])
# tall_non_identity = Matrix(elements = [[1,2],[2,4],[3,6]])
# wide_non_identity = Matrix(elements = [[1,2,3],[2,4,6]])

# (square_identity.rref()).show()
# (tall_identity.rref()).show()
# (wide_identity.rref()).show()
# (square_non_identity.rref()).show()
# (tall_non_identity.rref()).show()
# (wide_non_identity.rref()).show()

# a_has_inverse = Matrix(elements = [[1,0,1],[1,-1,2],[1,1,3]])
# a_wrong_size = Matrix(elements = [[1,2],[3,4],[5,6]])
# a_singular = Matrix(elements = [[1,2,3],[4,5,6],[7,8,9]])
# print("\nInverses:")
# (a_has_inverse.inverse()).show()
# (a_wrong_size.inverse()).show()
# (a_singular.inverse()).show()
# print("\nDeterminants:")
# print(a_has_inverse.determinant())
# print(a_wrong_size.determinant())
# print(a_singular.determinant())
# b_has_inverse = Matrix(elements = [[1,0,1],[1,-1,2],[1,1,3]])
# b_wrong_size = Matrix(elements = [[1,2],[3,4],[5,6]])
# b_singular = Matrix(elements = [[1,2,3],[4,5,6],[7,8,9]])
# print("\nInverse By Minors:")
# (b_has_inverse.inverse_by_minors()).show()
# (b_wrong_size.inverse_by_minors()).show()
# (b_singular.inverse_by_minors()).show()
# print("\nRecursive Determinants:")
# print(b_has_inverse.recursive_determinant())
# print(b_wrong_size.recursive_determinant())
# print(b_singular.recursive_determinant())

large_matrix = Matrix(elements = [[1, 2, 3, 4],[5, 0, 6, 0],[0, 7, 0, 8],[9, 0, 0, 10]])
larger_matrix = Matrix(elements = [[1.2, 5.3, 8.9, -10.3, -15],[3.14, 0, -6.28, 0, 2.71],[0, 1, 1, 2, 3],[5, 8, 13, 21, 34],[1, 0, 0.5, 0, 0.1]])
four_by_four_identity = Matrix(shape = [4,4], fill = 'diag')
five_by_five_identity = Matrix(shape = [5,5], fill = 'diag')
print("\nTesting Inverse for 4x4 Matrix:")
assert (large_matrix @ large_matrix.inverse()).round_down(6).elements == four_by_four_identity.elements,'Incorrect Inverse for large_matrix'
print("Passed")

print("\nTesting Inverse for 5x5 Matrix:")
assert (larger_matrix @ larger_matrix.inverse()).round_down(6).elements == five_by_five_identity.elements,'Incorrect Inverse for large_matrix'
print("Passed")

