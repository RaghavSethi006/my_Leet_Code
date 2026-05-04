class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels=[]
        index=set()
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                vovels.append(s[i])
                index.add(i)
        new_s=''
        for i in range(len(s)):
            if i in index:
                new_s+=vovels.pop()
            else:
                new_s+=s[i]
        return new_s
            

        