num = float(input())

if num < 10:
    print(int(num % 1 * 10))

elif num < 10 ** 7:
    print(int(num % 10 ** 6 * 10 % 10 ** 5 % 10 ** 4 % 10 ** 3 % 10 ** 2 % 10))

elif num < 10 ** 10:
    print(int(num % 10 ** 9 * 10 % 10 ** 8 % 10 ** 7 % 10 ** 6 % 10 ** 5 % 10 ** 4 % 10 ** 3 % 10 ** 2 % 10))

elif num < 10 ** 4:
    print(int(num % 10 ** 3 * 10 % 10 ** 2 % 10))
    
elif num < 10 ** 8:
    print(int(num % 10 ** 7 * 10 % 10 ** 6 % 10 ** 5 % 10 ** 4 % 10 ** 3 % 10 ** 2 % 10))


