ph_list = []
t= int(input("enter a number"))
for i in range(t):
    mun=int(input("enter a number"))
    ph_list.append(mun)
print(ph_list)
min=ph_list[0]
for j in ph_list:
    if min>j:
        min=j
print(min)