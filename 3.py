str1 = "sam"
print(str1)         # sam
print(type(str1))   # str

a = "10"            
print(a)            # 10
print(type(a))      # str

b = 20              
print(type(b))      # int

s = True
print(type(s))      # boolean

v = False
print(type(v))      # boolean

n = "False"
print(n)            # False
print(type(n))      #str

print(a,b,s,v,n,)   # 10 20 True False False

name = "sharifur rahman"
age = 20
marks = 82.876
print(name , "is", age , "years old and got the", marks ,
      "marks")                                                                # sharifur rahman is 20 years old and got the 82.876 marks
print("%s is %d years old and got the %f marks" %(name,age,marks))            # sharifur rahman is 20 years old and got the 82.876 marks

print(type(name))    # str
print(type(age))     # int
print(type(marks))   # float

print(f"{name} is {age} year old and got the {marks} marks")                 # sharifur rahman is 20 years old and got the 82.876 marks