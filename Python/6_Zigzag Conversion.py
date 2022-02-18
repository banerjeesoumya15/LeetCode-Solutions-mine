'''
https://leetcode.com/problems/zigzag-conversion/

Runtime: 54 ms, faster than 91.84% of Python3 online submissions for Zigzag Conversion.
Memory Usage: 14.1 MB, less than 74.23% of Python3 online submissions for Zigzag Conversion.
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        rows = [""] * min(numRows, len(s))
        curRow = 0
        goingDown = False
        
        for c in s:
            rows[curRow] += c
            if ((curRow == 0) or (curRow == numRows - 1)):
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow += -1
                
        ret = ""
        for row in rows:
            ret += row
            
        return ret
