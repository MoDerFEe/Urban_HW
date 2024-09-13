immutable_var = ('1',2,'urban',True)
print(immutable_var)
try:
    immutable_var[0]=3
except:
    print('Кортеж - неизменяем')

mutable_list=['1','2','3','4']
j=0
for i in mutable_list:
    mutable_list[j]=str(int(i)+1)
    j+=1

print(mutable_list)