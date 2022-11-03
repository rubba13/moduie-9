count = int(input('Введите кол-во билетов: '))
result = 0

for i in range(1, count + 1):
    age = int(input('Введите возраст участника {num}: '.format(num=i)))
    if 18 <= age < 25:
        result += 990
    elif age >= 25:
        result += 1390

if count > 3:
    result *= 0.9
    print('Скидка применена')
print('Итоговая стоимость билетов: ', result, " руб.")
