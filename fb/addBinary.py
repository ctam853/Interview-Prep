# Solution to LC: 67 Add Binary

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        anum = self.toInt(a)
        bnum = self.toInt(b)
        asum = anum + bnum
        if asum == 0:
            return "0"
        elif asum == 1:
            return "1"
        return self.toBinary(asum)
        
    
    
    def toInt(self, astr: str) -> int:
        power = 0
        total = 0
        for char in astr[::-1]:
            if char == "1":
                total += (2 ** power)
            power += 1
        return total
        
    def toBinary(self, anum: int) -> str:
        bstring = ""
        while anum != 0:
            if anum % 2 == 1:
                bstring = "1" + bstring
            else:
                bstring = "0" + bstring
            anum = anum // 2
        return bstring