number = int(input("Enter a Number:"))
count = 0
while number > 0:
    number = number // 10
    count += 1
print("The Number Of Digits in the given number is:", count)