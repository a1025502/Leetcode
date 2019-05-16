class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_a = sum(i for i in A if i % 2 == 0)
        
        for j in queries :
            if (A[j[1]] % 2 == 0) & (j[0] % 2 == 0):
                sum_a += j[0]
            elif (A[j[1]] % 2 != 0) & (j[0] % 2 != 0):
                sum_a += (j[0]+A[j[1]])
            elif (A[j[1]] % 2 == 0) & (j[0] % 2 != 0):
                sum_a -= A[j[1]]
                
            A[j[1]] +=j[0]
            ans.append(sum_a)

            
        return ans
            