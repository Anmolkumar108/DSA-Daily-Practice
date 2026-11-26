n = int(input("Enter Number: "))
num = n
total = 0
nod = len(str(n))
while num > 0:
    digit = num % 10
    total = total + (digit ** nod)
    num = num // 10
if n == total:
    print(f"{n} is Armstrong Number")
else:
    print(f"{n} is Not Armstrong Number")
