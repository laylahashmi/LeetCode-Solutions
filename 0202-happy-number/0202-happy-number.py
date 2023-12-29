class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n != 1:
            n = sum([int(d)**2 for d in str(n)])
            if n in sums:
                return False
            sums.add(n)
        return True
    


        