class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 =set("zxcvbnm")
        ans = []
        for i in words:
            input_list = set(i.lower())
            if row1 & input_list == input_list:
                ans.append(i)
            if row2 & input_list == input_list:
                ans.append(i)
            if row3 & input_list == input_list:
                ans.append(i)
                
        return ans