class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
            
        lst =[]
        
        for i in range(len(nums)+1):
            lst.append(i)
        res = set(lst)-set(nums)
        if len(res)>0:
            return list(res)[0]
        else:
            return
