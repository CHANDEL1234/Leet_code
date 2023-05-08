class Solution:
    def intToRoman(self, number: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I  = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ans = []
        num = str(number)
       
        x = len(num)
        for i in range(x,0,-1):
            if i == 4:
                res = M[int(num[abs(i-x)])]
                ans.append(res)
            if i == 3:
                res = C[int(num[abs(i-x)])]
                ans.append(res)
                print(i)
            if i ==2:
                res = X[int(num[abs(i-x)])]
                ans.append(res)
            if i ==1:
                res = I[int(num[abs(i-x)])]
                ans.append(res)
            
         
        return ("".join(ans))
