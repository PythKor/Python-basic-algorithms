num=20

a=[]
for i in range(num):
    v1=float(input())
    a.append(v1)

b=[]
for i in range(num):
    v1=float(input())
    b.append(v1)

new_list=[]

for i in range(num):
    if a[i] > b[i]:
        new_list.append(a[i])
    else:
        new_list.append(b[i])

print(a)
print(b)
print(new_list)
