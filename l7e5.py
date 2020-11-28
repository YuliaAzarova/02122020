n = int(input())
pluss = 0
minus = 0
ziro = 0
for x in range(n):
    a = int(input())
    if a > 0:
        pluss += 1
    if a < 0:
        minus += 1
    if a == 0:
        ziro += 1
print(ziro)
print(pluss)
print(minus)