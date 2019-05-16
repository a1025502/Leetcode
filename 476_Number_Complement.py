class Solution:
    def findComplement(self, num: int) -> int:
        
        a =1 << len(bin(num))-2
        a -= 1
        
        return num ^ a