class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = [i]
            for j in range(len(nums)):
                if i==j:
                    pass
                else:
                    if (nums[i]+nums[j]) == target:
                        temp.append(j)
                        return temp 
        