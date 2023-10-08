## Task 1
given_string = input()
print(given_string[::-1])

## Task 2
given_string = input()
given_index = int(input())
print(given_string[given_index::-1] + given_string[given_index+1:])

## Task 3
n = input()
Binary = True

for i in n:
  if i != "0" and i != "1":
    Binary = False

if Binary == True:
  print("Binary Number")
else:
  print("Not a Binary Number")

## Task 4
user = input()
new = ""

if(len(user) < 4):

    if user.endswith("er"):
        new = user[0:1] + "est"
        print(new)
    else:
        new = user
        print(new)

elif(len(user) > 3):

    if not user.endswith("er") and not user.endswith("est"):
        new = user+"er"
        print(new)
    if user.endswith("er"):
        new = user[0:-2]+"est"
        print(new)
    elif user.endswith("est"):
        new = user
        print(new)

## Task 5
n = input("Enter a String: ")
j = len(n)
for row in range(j):
  for col in range(row+1):
    print(n[col],end="")
  print()

## Task 6
n = input("Enter a string: ")
for i in n:
  print(i,":", ord(i))

## Task 7
user_input = input("Enter a string: ")
new_word = ""
for i in range(len(user_input)):
  if user_input[i] == 'z':
    new_word += 'a'
  else:
    next_alphabet = chr(ord(user_input[i])+1)
    new_word += next_alphabet
print(new_word)

## Task 8
user = input("Enter any string: ")
new = ''
for i in range(len(user)):
  if i % 2 != 0:
    if 65<=ord(user[i])<=90:
      new += user[i]
    else:
      cap = chr(ord(user[i]) - 32)
      new += cap
print(new)

## Task 9
user = input("Enter a string: ")
new = ""
for letter in user:
  if new == "" or letter != new[len(new) - 1]:
    new += letter
print(new)

## Task 10
s1 = input("Enter the 1st string: ")
s2 = input("Enter the 2nd string: ")
i = 0
j = 0
sum = ""
while i<len(s1) or j<len(s2):
  if i<len(s1):
    sum = sum + s1[i]
    i += 1
  if j<len(s2):
    sum = sum + s2[j]
    j += 1
print(sum)

## Task 11
# Tracing 1

i = 10
while(i >= -20):
    if(i < 0):
        test = " != "
        test = str(i//2) + test + str(int(i/2))
    else:
        test = " == "
        test = str(i//2) + test + str(int(i/2))
    print(test)
    i -= 5

## Task 12
# Tracing 2
test = ""
i = 0
j = 0
k = 15
test = "-->"
while i < 5:
    j = k - 1
    k -= 1
    while j > 10:
        test = str(i + j) + "-->" + test
        print(test)
        j -= 1
    i += 1

## Task 13
# Tracing 3
test = ""
i = 5
j = 0
k = 15
while i< 10:
    k-=1
    j = k
    while j > 10:
        if (j % 2) == 0:
            test = "<--"
            test = str(test) + str(i) + str(2) + "-->" + str(int(j / 2))  
        else:
            test = "-->"
            test = "-->" + str(int(i / 2)) + str(test) + str(j)
        print(test)
        j = j-1
    i+=1

## Task 14
# Tracing 4
test = ""
i = 5
j = 0
k = 15
while (i< 10): 
    k-=1
    j = k
    while (j > 10 ):
        if j % 2 == 0:
            test = "<--"
            test = test + str( i) + '3' + "-->" + str(j // 3)
        else:
            test = "-->"
            test = "-->" + str((i // 3)) + test + str(j)
        print(test)
        j -=1
    i+=1

## Task 15
# Tracing 5
i=0
j=0
k=15
test = '<--cat'
while i < 5:
    k -= 1
    j = k
    while j > 10:
        if j % 2 == 0:
            test += '-->'
            test = test + str(i) + str(j // 2)
        else:
            test += '<--'
            test = test + str(i // 2) + str(j)
        print(test)
        j-=1
    i+=1
