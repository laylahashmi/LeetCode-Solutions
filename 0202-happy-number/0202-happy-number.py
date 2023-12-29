class Solution:
    def isHappy(self, n: int) -> bool:
        sums = []
        while n != 1:
            digits = [int(d)**2 for d in str(n)]
            n = sum(digits)
            if n in sums:
                return False
            sums.append(n)
        return True
    


        