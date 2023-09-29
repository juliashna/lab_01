a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

a1 = a
b1 = b
while(a!=0 and b!=0):
    if (a>b):
        a = a % b
    else:
        b = b % a
print("НОД числа",a1,"и числа",b1,"равен",a+b)