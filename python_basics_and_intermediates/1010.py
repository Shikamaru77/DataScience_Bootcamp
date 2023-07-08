it1= input().split()
it2= input().split()
res=0
a,b,c =it1
d,e,f=it2
res += ((float(b)*float(c))+(float(e)*float(f)))
#d= int(input())
#print("NUMBER =",a)
print("VALOR A PAGAR: R$ %.2f"%res)