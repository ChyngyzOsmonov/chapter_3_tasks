T = int(input())
while T != 0:
    s = input()
    l = len(s)
    f = 0
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        try:
            if i == ')' and stack[-1] == '(':
                f += 1
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                f += 1
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                f += 1
                stack.pop()
        except IndexError:
            continue
    if f==l/2 and l % 2 == 0:
        print("YES")
        T -= 1
    else:
        print("NO")
        T -= 1