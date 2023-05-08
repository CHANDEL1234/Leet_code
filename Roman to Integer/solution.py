class Solution:
    def romanToInt(self, s: str) -> int:
        
    
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I  = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ans = 0
        if "CM" in s:
            ans += 900
            s=s.replace("CM", "")
        if "CD" in s:
            ans += 400
            s=s.replace("CD", "")
        if "XL" in s:
            ans += 40
            s=s.replace("XL", "")
        if "XC" in s:
            ans += 90
            s=s.replace("XC", "")
        if "IV" in s:
            ans += 4
            s=s.replace("IV", "")
        if "IX" in s:
            ans += 9
            s=s.replace("IX", "")
        for char in s:
            if char in M:
                ans += M.index(char)*1000
            if char in C:
                ans += C.index(char)*100
            if char in X:
                ans += X.index(char)*10
            if char in I:
                ans += I.index(char)*1
        return ans
