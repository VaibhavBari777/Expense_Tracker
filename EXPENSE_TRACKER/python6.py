

#Experiment FUNCTION
#function without argument
def myfunction():
    print("This is myfunction")
myfunction()
#function with argument
def myfunction(p):
    print("The no. is:",p)
a=3
myfunction(a)
def myfunction(p,q):
    print("The sum is:",(p+q))
a=3
b=10
myfunction(a,b)
def myfunction(p,q):
    c=p+q
    print("The sum is:",c)
a=3
b=10
myfunction(a,b)
def myfunction(p,q):
    r=p+q
    return r
a=3
b=10
x=myfunction(a,b)
print(x)
def myfunction(p,q=12):
    r=p+q
    print(r)
a=3
b=10
myfunction(a,b)
def myfunction(p,q=12):
    r=p+q
    print(r)
a=3
b=10
myfunction(a)
#recursive function factorial
def factofno(n):
    if(n==1):
        return 1
    else:
        return(n*factofno(n-1))
factoutput = factofno(5)
print("Theb factorial is",factoutput)