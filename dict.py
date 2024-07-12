#syntax of dictionary 
d={}#empty dictionary  
marks={
    "hary":100
    ,"rohan":200
    ,"mohit":300
}
print(type(marks))
print(marks,type(marks))
print(marks["mohit"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"hary":99})
print(marks)
s=set()
print(s,type(s))
w={}
print(w,type(w))
l=[2,4,5,1]
l.sort()
print(l)
s={}
name=input("enter the friends name:")
lang=input("enter the language:")
s.update({name:lang})
name=input("enter the friends name:")
lang=input("enter the language:")
s.update({name:lang})
name=input("enter the friends name:")
lang=input("enter the language:")
s.update({name:lang})
name=input("enter the friends name:")
lang=input("enter the language:")
s.update({name:lang})
name=input("enter the friends name:")
lang=input("enter the language:")
s.update({name:lang})
print(s)
print(s.items())
print(type(s))
