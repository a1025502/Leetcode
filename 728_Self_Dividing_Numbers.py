class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        bound = []
        for i in range(left,right+1):
            bound.append(i)
        ans = []
        for j in bound:
            flag = 0
            divid = list(str(j))
            if '0' in divid:
                continue
            for k in divid:
                if j % int(k) != 0:
                    flag = 1
                    break
            if flag == 1:
                continue
            ans.append(j)
        return ans
            