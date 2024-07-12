n=int(input("enter the no"))
p=1
for i in range(1,n+1):
    p=p*i
    print(p)

print(p)
p=int(input("enter the no"))
for j in range (1,p+1):
    print(" "*(p-j),end="")
    print("*"*(2*j-1),end="")
    print("")

def avg():
    p=int(input("enter the no"))
    q=int(input("enter the no"))
    r=int(input("enter the no"))
    avegage=(p+q+r)/3
    print(avegage)

avg()
def greet(name):
    gr="hello"+name
    return gr

a=greet(" "+"sai")
print(a)
def goodday(name,ending="Thanking you"):
    print(f"good day,{name}")
    print(ending)

goodday("sai","Thank You")