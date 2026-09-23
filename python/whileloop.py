# i =1
# while i<6:
#     print(i)
 #     i=i+1



# wapt to print no from 1 to 20
# i = 1
# while i<21 :
 #     print(i)
#     i = i+1

# i = 2
# while i<21 :
#     if i % 2 == 0:
#         print("even numbers are:",i)
#     i = i+1

# a = int(input("Enter your no. :"))
# i = a[1]

# while i <len(a) + 1 :
#     print(i+a[])


# match = 1+2
# print(match)

# a=input("Enter your word:")

# b=a.lower()
# total_vowels = 0
# i=0

# while i <len(b):
#    word= b[i]
#    if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
#       total_vowels = total_vowels + 1
#    i = i + 1

# print(total_vowels)

#break statement is used to exit a loop prematurelly when a specific condition is meet
# i = 1 
# while i < 6:
#    print(i)
#    if i == 3:
#       break
#    i = i + 1



#continue statement is used to skip current iteration of a loop when a specific condition is meet and it continues with the next iteration of the loop.
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

a = input("Enter your word:")
b = a.lower()
total_vowels=0
vowels = "aeiou"

for i in range(0,len(b)):
    if b[i] in vowels:
        total_vowels += 1

print(total_vowels)