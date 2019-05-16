class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        length = len(A)
        ans = [None] * length
        even = 0
        odd = 1
        for i in range(len(A)):
            if A[i] % 2 == 0 :
                ans[even] = A[i]
                even += 2
            else:
                ans[odd] = A[i]
                odd += 2
            
        return ans