# converting an integer into decimal
import decimal
i =10
print(decimal.Decimal(10))
print (type(decimal.Decimal(i)))
# converting an string into decimal
import decimal
stri="321"
print(decimal.Decimal(stri))
print (type(decimal.Decimal(stri)))
# reverse string 
string ="priyanka"
print (string[::-1],"is reverse of string" )
# counting the vowel
strp=input("enter a string")
vowel=["a","e","i","o","u"]
count=0
for i in strp:
    if i in vowel:
        count+=1
print(count)
# counting the consonants:
stree=input("enter a string")
vowel=["a","e","i","o","u"]
times=0
for i in stree:
    if i not in vowel:
        times+=1
print(times)
# counting no of occurence:
word=input("enter a word")
text="r"
number=0
for i in word:
    if i ==text:
        number+=1
print(number)
# writing fibonacci series:
n=int(input("enter a number"))
fib=[0,1]
for i in range(n):
    fib.append (fib[-1]+fib[-2])
print(".".join(str(e) for e in fib))
# finding the max number in a list 
num_list = []
n = int(input("Enter how many numbers: "))

for i in range(n):
    num = int(input("Enter a number: "))
    num_list.append(num)

print (num_list)
max=num_list[0]
for j in num_list:
    if max<j:
        max=j
print(max)
# finding the max number in a list 
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
# finding the mid element of a list
pri_list=[]
k=int(input("Enter how many numbers: "))
for i in range(k):
    ijk=int(input("enter a number"))
    pri_list.append(ijk)

print (pri_list)
mid_element=int(len(pri_list)/2)
print(mid_element)
                
