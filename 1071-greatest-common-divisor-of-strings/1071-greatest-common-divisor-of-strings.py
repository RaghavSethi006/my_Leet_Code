class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1<str2:
            small=str1
        else:
            small=str2
        temp=""
        sol=""
        for i in small:
            temp+=i
            temp2=set(str1.split(temp))
            temp3=set(str2.split(temp))
            if temp2 == temp3=={""}:
                sol=temp
        return sol
        