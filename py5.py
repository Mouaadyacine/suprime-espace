a=input("enter a string")
b=""
for i in range(len(a)):
    if a[i]!=" ":
        b=b+a[i]
print(b)