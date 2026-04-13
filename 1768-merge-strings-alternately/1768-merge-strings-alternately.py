class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        temp=[]
        while i<len(word1) or j <len(word2):
            if i<len(word1):
                temp.append(word1[i])
            if j<len(word2):
                temp.append(word2[j])
            i+=1
            j+=1
        temp=''.join(temp)
        return temp