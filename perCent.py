# Ставки
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму вклада: "))
deposit = [int(value * money / 100) for value in per_cent.values()]
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
