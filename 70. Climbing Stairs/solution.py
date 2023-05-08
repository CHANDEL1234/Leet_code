class Solution:
    import math
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        ans =0
        lst = []
        if n%2==0:
            for i in range(n//2):
                lst.append(2)
        if n%2==1:
            for i in range(n//2):
                lst.append(2)
            lst.append(1)
        
        while lst.count(2)>=0 and lst.count(1)<=n:
            two = lst.count(2)
            one = lst.count(1)
            
            
            
            ans += (math.factorial(len(lst)))//(math.factorial(two)*math.factorial(one))
            
            if lst.count(2)>0:
                lst.remove(2)
            lst.append(1)
            lst.append(1)
            
        return ans
        
