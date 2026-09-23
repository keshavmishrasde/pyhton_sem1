a="hello!"
b="How are you?"
c=a+b
print(c)

# d=10
# e="years"
# print(d+e) error because you cannot add oe int type and another string


# f-string
# to create f-string prefix f in front of the string and {} as placeholder for variables and other operation

age=17
n="keshav"
text=f"my name is {n},i am {age} years old"
print(text)

eng,maths,hindi = 67,78,80
print(f"Ram got total marks {eng+maths+hindi}")