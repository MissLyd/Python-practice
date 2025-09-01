class Solution:

    def convert(self,s,numRows):
        # Starting with an empty string
        solution=""
        # Going through each row
        for row in range(numRows):
            # Going from the row to the end of the string and incrementing
            for i in range(row,len(s),(numRows-1)*2):
                # prints first character on the row
                solution+=s[i]
                # If the row is in the middle, prints other character on the row BEFORE the ones in the incrementation
                if (row>0 and row <numRows-1 and (numRows-1)*2-2*row<len(s)):
                    solution+=s[i+(numRows-1)*2-2*row]

        return solution

s="PAYPALISHIRING"
numRows=3
solution=Solution()
print(solution.convert(s,numRows))