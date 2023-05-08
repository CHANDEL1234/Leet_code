class NumArray:

    def __init__(self, nums: List[int]):
        self.add = list()
        self.add.extend(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        res = 0 
        for i in ((self.add[left:right+1])):
            res += i
        return res
