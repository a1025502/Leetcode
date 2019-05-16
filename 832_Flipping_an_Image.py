class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        matrix_reversed = []
        matrix_invert = []
        ans = []
        for i in A:
            matrix_reversed.append(list(reversed(i)))
            
        for j in matrix_reversed:
            matrix_invert = list(map(lambda a : 0 if a == 1 else 1 , j))
            ans.append(matrix_invert)
        return (ans)