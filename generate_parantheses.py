
def solution(n):
    result=[]

    def backtracking(openN,closeN,s):
        if openN==closeN==n:
            result.append(s)

        if openN<n:
            backtracking(openN+1,closeN,s+"(" )

        if closeN<openN:
            backtracking(openN,closeN+1,s+")")
        
    backtracking(0,0,"")
    return result
    
while True:
    n=int(input("Enter a number between 1 and 8: "))
    if 1<=n<=8:
        break
    else:
        continue

print(solution(n))
