
x=lambda a:print(a)
x(10)

addition=lambda p,q:p+q
print("The addition is:", addition(35,25))

subtraction=lambda s,t=50:s-t
print("The subtraction is:", subtraction(100,65))



a=[10,20,30,40,50,60]
print(type(a))
print(a)
def myfunction(n):
  return n+5
output=list(map(myfunction,a))
print("The updated list a is:", output)


b=[10,20,30,40,50,60]
print(type(b))
print(b)
output2=list(map(lambda n:n+5, b))
print("The updated list b is:", output2)


c=[10,80,20,30,40,50,60,90,120,100,35,65,85,95,25,76]
print(type(c))
print(c)
def myfunction2(n):
  if n>=40:
    return True
output3=list(filter(myfunction2,c))
print("The updated list c is:", output3)
d=[True,False,False,True,True, False,False,True,False]
print(type(d))
print(d)
output4=list(filter(None,d))
print("The updated list d is:", output4)



e=[10,80,20,30,40,50,60,90,120,100,35,65,85,95,25,76]
print(type(e))
print(e)
output5=list(filter(lambda n:n>=40, e))
print("The updated list e is:", output5)

import functools
f=[10,20,30,40,50,60,70,80,90,100]
print(type(f))
print(f)
output6=functools.reduce(lambda m,n:m+n,f)
print("The final sum is:", output6)


list1=["branch","class", "subject","practicals","marks"]
list2=["AIML", "SY","python",2,50]
list3=list(zip(list1,list2))
print("The zipped lists are:", list3)