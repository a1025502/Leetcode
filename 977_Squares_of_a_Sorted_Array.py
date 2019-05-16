class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = []
        for i in range(len(A)):
            squares.append(A[i]**2)
        squares.sort()
        
        return squares