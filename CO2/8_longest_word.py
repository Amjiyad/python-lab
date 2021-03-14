l1=[]
m=[]
print("enter the words")
for i in range(3):
    n=input()
    m.append(len(n))
    l1.append(n)
print(l1)
print("length of longest word:",max(m))
    
