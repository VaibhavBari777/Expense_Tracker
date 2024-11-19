
f=10
if f>1 and f<20:
    print("The number is 10.")
else:
    print(" The number is not 10.")

# if elif else
f=10
if f>10:
    print("The number is greater than 10.")
elif f<10:
    print("The number is less than 10.")
else:
    print("The number is exactly 10.")
## elif ladder
marks=int(input("Enter the marks"))
if (marks >0 and marks <40):
  print("Fail")
elif (marks >=40 and marks <60):
  print("Second class")
elif (marks >=60 and marks <75):
  print("First class")
else:
  print("Distinction")