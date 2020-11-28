n = int(input("Введите число < 20:"))
n = str(n)
chet = 0
col_num = len(n)
if col_num > 20:
    exit(print("Error: цифр в числе больше 20!")
    )
for x in range(col_num):
    if int(n[x]) % 2 == 0:
        chet += 1
print(chet)