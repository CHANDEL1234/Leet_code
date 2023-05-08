class Solution:
    def maxArea(self, height: List[int]) -> int:
        res =[]
        i = 0
        j = len(height)-1
        while j-i >0:
            area = min(height[i], height[j])*abs(j-i)
            res.append(area)
            if height[j]<=height[i]:
                 j -= 1
            else:
                i += 1
            
        return max(res)
