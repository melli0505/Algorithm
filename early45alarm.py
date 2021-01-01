H, M = map(int, input().split())

if M >= 45:
    M -= 45
else:
    temp = 45 - M
    M = 60 - temp
    if H == 0:
        H = 23
    else: H -= 1

print(H, M)