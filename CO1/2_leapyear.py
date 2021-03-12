cy=int(input("enter the current year"))
fy=int(input("enter the final year"))
print("leap years are")
for i in range(cy,fy+1):
    if i%4==0:
        print(i)
