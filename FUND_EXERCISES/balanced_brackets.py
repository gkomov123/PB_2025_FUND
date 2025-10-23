n = int(input())
last_was_open = False
balanced = True

for i in range(n):
    line = input()
    if line == "(":
        if last_was_open == True:
            balanced = False
            break
        last_was_open = True
    elif line == ")":
        if last_was_open == False:
            balanced = False
            break
        last_was_open = False
    else:
        continue

if last_was_open == True:
    balanced = False

if balanced == True:
    print("BALANCED")
else:
    print("UNBALANCED")


