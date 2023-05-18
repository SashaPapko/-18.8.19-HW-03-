numtickets = int(input("Сколько билетов вы хотите приобрести? "))

totalcost = 0
discount = 0

for i in range(numtickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        totalcost += 0
    elif age < 25:
        totalcost += 990
    else:
        totalcost += 1390

if numtickets > 3:
    discount = 0.1 * totalcost
    totalcost -= discount

print("Общая стоимость билетов: ", totalcost)