class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I':[1,1],
            'V':[2,5],
            'X':[3,10],
            'L':[4,50],
            'C':[5,100],
            'D':[6,500],
            'M':[7,1000]
        }
        rank,value=0,1
        sum=0
        for i in range(len(s)):
            if i!=len(s)-1:
                if symbol[s[i]][rank]<symbol[s[i+1]][rank]:
                    sum-=symbol[s[i]][value]
                else:
                    sum+=symbol[s[i]][value]
            else:
                sum+=symbol[s[i]][value]
        return sum

        
        