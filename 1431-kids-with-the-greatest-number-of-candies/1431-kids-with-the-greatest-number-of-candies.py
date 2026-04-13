class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        for i in range(len(candies)):
            temp=candies.copy()
            temp[i]+=extraCandies
            max_var = max(temp)
            if max_var == temp[i]:
                res.append(True)
            else:
                res.append(False)
        return res

    def max(self,arr:List[int])->int:
        temp=arr[0]
        for i in arr:
            if i>temp:
                temp=i
        return temp
        