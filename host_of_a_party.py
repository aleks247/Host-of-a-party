#Не знам как да напиша текста за Input-a 
initial_bites = int(input())

guests = []

# Прочитаме имената на гостите и ги добавяме към list-a 'guests' 
while True:
    command = input()
    if command == "Start":
        break
    guests.append(command)

taken_bites = []

# Четем командите "Take" или "Refill" и изпълняваме съответните действия
while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        # Ако командата е "Refill", извличаме количеството на хапките и го добавяме към текущите хапки
        #_ е променлива която приема refill от input-а и за beets остава другата стойност
        _, beets = command.split()
        initial_bites += int(beets)
    else:
        # Ако командата не е "Refill", предполагаме, че тя е количество хапки, които се искат от текущия гост
        # Проверяваме дали има гости в списъка guests
        if guests:
            #Придава стойноста на guest от първия елемент на List-a 'guests' и я премахва от него
            guest = guests.pop(0)
            # Проверяваме дали има достатъчно хапки в платото
            bites = int(command)  # Определяме количеството на хапките от командата
            if initial_bites >= bites:
                # Ако има, добавяме информация за взимането на хапки и намаляваме наличните хапки
                taken_bites.append(f"{guest} take bites")
                initial_bites -= bites
            else:
                # В противен случай, ако няма достатъчно хапки, добавяме информация, че гостът трябва да чака
                taken_bites.append(f"{guest} must wait")
        else:
            # Ако няма гости в списъка loop-а спира
            break

# Изпечатваме информацията за взимането на хапки и кой трябва да чака
for bite in taken_bites:
    print(bite)

print(f"{initial_bites} bites left")
