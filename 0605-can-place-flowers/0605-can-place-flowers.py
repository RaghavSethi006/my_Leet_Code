class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        sum=0
        if len(flowerbed)- flowerbed.count(1) < n : return False
        if flowerbed==[0] and n==1 : return True
        if len(flowerbed)>1:
            if flowerbed[0]==flowerbed[1]==0:
                sum+=1
                flowerbed[0]=1
            if flowerbed[-1]==flowerbed[-2]==0: 
                sum+=1
                flowerbed[-1]=1
        for i in range(1,len(flowerbed)-1):
            left=flowerbed[i-1]
            index=flowerbed[i]
            right=flowerbed[i+1]
            if left==index==right==0:
                sum+=1
                flowerbed[i]=1

        if flowerbed==[0,0]: sum = 1
      
        return sum>=n
