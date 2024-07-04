first = (int(input("Введите число: ")))
second = (int(input("Введите 2е число: ")))
third = (int(input("Введите 3е число: ")))
if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
