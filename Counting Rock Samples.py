a , t =  map(int,input().split(' '))
arr= list(map(int,input().split(' ')))
ans =[]
c = 0 
n1= 0
n2 = 0
for i in range(t):
    n1,n2 = map(int,input().split(' '))
    for j in arr:
        if j in range(n1,n2+1):
            c += 1
    ans.append(c)
    c = 0
print (*ans)
