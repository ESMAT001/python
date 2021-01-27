

# num=int(input())
# if num>0:
#     print("+")
# elif num==0:
#     print("0")
# else:
#     print("-")

# n=input()
# print(n.upper())

# a=input()
# if a.isupper():
#     print(a.lower())
# else: 
#     print(a)
a=int(input())
if a%3==0 and a%5==0:
    print("fizz buzz")
elif a%3==0:
    print("fizz")
elif a%5==0:
    print("buzz")