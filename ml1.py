import re
import time
#1
s=input()
print(s[::-1])

#2
s=input().split()
for i in s:
    print(i[0],end="")

#3
s=input().split()
st=""
for i in s:
    for j in i:
        if j.isupper()==True:
            st+=j
print(st)

#4
s=input().split()
print(s.reverse())

#5
import re
data=" "+input("Enter sentence:")+" "
pat=""+input("Enter pattern:")+"\w*"
pat=re.compile(pat)
res=re.findall(pat,data)
for i in res:
    print(i)
res

#6
#append : Adds its argument as a single element to the end of a list. The length of the list increases by on
l1=[1,2]
l1.append([3])
print(l1)
#extend: Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.
l1=[1,2]
l1.extend([3])
print(l1)

#7
x=True
y=True
a=(not (x or y))==(not x and not y)
b=(not(x and y))==(not x or not y)
print(a,b)

#8
a,b,c,l,t1=[x for x in range(1,100000000)],[].[],0,time.time()
for i in a:
    b.append(i*i)
t1=time.time()-t1
print("time for for loop:",t1*1000)
t2=time.time()
while l<len(a):
    c.append(a[l]*a[l])
    l+=1
t2=time.time()-t2
print("time for while loop is :",t2*1000)

