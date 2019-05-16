class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = list(f'{x:032b}')
        y = list(f'{y:032b}')
        ans = 0
        for i in range(32):
            if x[i] != y[i]:
                ans +=1
                
        return ans