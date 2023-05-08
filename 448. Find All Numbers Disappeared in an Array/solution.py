class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        set_1 = set(nums)
        set_2 =set()
        for i in range(1, len(nums)+1):
            set_2.add(i)
        return list(set_2-set_1)
