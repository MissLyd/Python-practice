class Solution:
    def solveNQueens(self, n):

        cols=set()
        PosDiag=set()
        NegDiag=set()

        sol = []
        board = [["."]*n for _ in range(n)]

        def backtrack(r):
            if r==n:
                board_copy = ["".join(row) for row in board]
                sol.append(board_copy)
                return

            for c in range(n):
                if c in cols or (r+c) in PosDiag or (r-c) in NegDiag:
                    continue
                
                cols.add(c)
                PosDiag.add(r+c)
                NegDiag.add(r-c)
                board[r][c]="Q"
                
                backtrack(r+1)

                cols.remove(c)
                PosDiag.remove(r+c)
                NegDiag.remove(r-c)
                board[r][c]="."

        backtrack(0)
        return sol
    
sol = Solution()
while True:
    try: 
        n = int(input("Enter an integer between 1 and 9: "))
        if n<1 or n>9:
            print("Enter an integer between 1 and 9: ")
        else:
            break
    except ValueError:
        print("Enter a number.")


res = sol.solveNQueens(n)
print(res)