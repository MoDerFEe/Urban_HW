a=str(input(''))
print(a[0])
print(a[-1:])
print(a[-(len(a)//2 if len(a)%2==0 else len(a)//2+1):])
print(a[::-1])
j=0
k=''
for i in a:
    if j%2!=0:
        k+=i
    j+=1
print(k)