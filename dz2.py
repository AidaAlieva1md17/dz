'Нахождение вагона'
number=int(input ("Введите номер вагона:  "))
print()
if number>36:
        print("Ваше место боковое.")
if number%2:
    print("Ваше место в купе внизу.")
else:
    print("Ваше место в купе наверху.")