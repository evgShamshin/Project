# стартовое количество организмов
m = int(input())
# среднесуточное увеличение в %
p = int(input())
# количество дней для размножения
n = int(input())

print(1, m)

# Записываем переменную саму в себя
# Так же формула подходит для капитала и процентов
for j in range(2, n + 1):
    m = m + m * p / 100
    print(j, m)
