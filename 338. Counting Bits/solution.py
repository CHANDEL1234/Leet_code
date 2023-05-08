class Solution:
    def countBits(self, n: int) -> List[int]:
        res = list()
        for i  in range(n+1):
            bin_ = str(bin(i))
            count_ =  bin_.count("1")
            res.append(count_)
        return res
