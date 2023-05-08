class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans= ""
        
        minimum_len = min(strs)
        for  i in range(0, len(minimum_len)):
            current = strs[0][i]
            for j in range(0, len(strs)):
                if current != strs[j][i]:
                    return ans
            ans += current
        return ans
