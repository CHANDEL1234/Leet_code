class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        def binary_search(nums , target, low , high):
            if low>high:
                return -1
            mid = (low + high)//2

            if nums[mid] == target:
                return mid
            if nums[mid]<target:
                low = mid+1
                return binary_search(nums,target, low, high)
            if nums[mid]>target:
                high = mid-1
                return binary_search(nums, target, low, high)
            
        return binary_search(nums, target, low, high)
