n=int(input("enter a number:"))
p=5
q=3
r=1
s=0
for i in range(0,n):
    if i<3:
        for j in range(0,s):
            print(" ",end=" ")
        s=s+1
        for j in range(0,p):
            print("*",end=" ")
        p=p-2
        print()
    elif i>=3:
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(q):
            print("*",end=" ")
        q=q+2 
        print()   
        
# for i in range(n-3):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(q):
#         print("*",end=" ")
#     # q=q+2
#     # print()        5
