import os

print("hello world")
word = input()


def read(word):
    return len(word)


print(f"it has {read(word)} chars")

var = input("shut down?")
if var == "no":
    exit()
# else:
    # os.system("shutdown /s /t 10")
