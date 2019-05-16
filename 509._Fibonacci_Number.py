class Solution:
    def fib(self, N: int) -> int:
        f_0 = 0
        f_1 = 1
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            for i in range(N-1):
                f_n = f_0 + f_1
                f_0 = f_1
                f_1 = f_n
                
            return f_n
            
        