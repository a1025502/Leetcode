class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        ans = []
        for i in range(len(A)):
            if (A[i] % 2 == 0):
                even.append(A[i])
            else:
                odd.append(A[i])
        ans = even + odd        
        return ans