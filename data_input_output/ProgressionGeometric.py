'''первый член геометрической прогрессии'''
b1 = int(input())
'''знаменатель геометрической прогрессии '''
q = int(input())
'''число геометрической прогрессии'''
n = int(input())

output = b1 * q ** (n - 1)
print (output)