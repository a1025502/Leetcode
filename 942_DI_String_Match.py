class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        a = []
        for i in range(1+len(S)):
            a.append(i)
        ans = []
        for s in S:
            if s == 'I':
                ans += [a.pop(0)]
            else :
                ans += [a.pop()]
                
        ans += [a.pop()]
        
        return ans
            