class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        a = 0
        for i in range(len(A)):
            if A[i]<A[i+1]:
                a +=1
            else:
                break
                
        return a