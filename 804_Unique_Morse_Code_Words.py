class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
                 "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
                 ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            morse_code = ''
            for num in  word:
                morse_code = morse_code + morse[ord(num)-ord('a')]
            ans.add(morse_code)
                
        return len(ans)