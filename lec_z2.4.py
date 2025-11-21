n = int(input("Введите количество элементов ряда Фибоначчи: "))

if n <= 0:
    print("Ошибка: число должно быть натуральным ")
else:
    a, b = 1, 1
    print("Ряд Фибоначчи:")
    
    if n >= 1:
        print(a, end=' ')
        
    if n >= 2:
        print(b, end=' ')
        
    for i in range(2, n):
        c = a + b
        print(c, end=' ')
        a, b = b, c
    print()  
