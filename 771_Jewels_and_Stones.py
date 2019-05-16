class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        a = 0
        for i in J:
            a = a + S.count(i)
            
        return a
        