def sum(n):
    global s
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

print(s)

