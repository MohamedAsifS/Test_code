class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack=[]
        current=0

        for i in range(len(word)):
            if word[i]!=ch:
                stack.append(word[i])
            else:
                stack.append(word[i])
                current=i
                break
        if current==0:
            return word
       
        res=""
        while stack:
            res+=stack.pop()

        return res+word[current+1:len(word)]

        