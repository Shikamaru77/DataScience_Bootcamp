a,b,c = map(int,input().split())
res = ((a+b+abs(a-b))/2)
resSS= ((res+c+abs(res-c))/2)
print("%d eh o maior" %resSS)