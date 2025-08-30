A=[1,3,8,9,15]
B=[7,11,18,19,21,25]

n,m =len(A),len(B)
Px=int((n-1)/2 )
Py=int((n+m-1)/2-Px)

print(Px,Py)

while A[Px-1]>B[Py] or B[Py-1]>A[Px]:
    if A[Px-1]>B[Py]:
        Px-=1
    else:
        Px+=1
    Py=int((n+m+1)/2-Px)

if n+m%2==0:
    med=(max(A[Px-1],B[Py-1])+min(A[Px],B[Py]))/2
else:
    med=max(A[Px-1],B[Py-1])

print(med)


