import random
def ugadai_chislo(i):
    print("Гра вгадай число. Програма загадує число від 0 до 100, а гравець повинен вгадати")
    programe_chislo = int(random.random() * 100)
    while(1):
        user_chislo = int(input("Введіть число від 0 до 100. Для виходу з гри -1 "))
        if user_chislo == -1:
            break
        elif user_chislo > programe_chislo:
            print("Ваше число завелике")
        elif user_chislo < programe_chislo:
            print("Ваше число замале")
        elif user_chislo == programe_chislo:
            print("Вітаю! Ви вгадали число! Кількість спроб: ", i)
            break
        else:
            print("Error")
            continue
        i+=1
def krestiki_noliki():
    first_ryad = [1 , 1 , 1]
    second_ryad = [1 , 1 , 1]
    third_ryad = [1 , 1 , 1]
    a = 0;
    def perevirka(x):
        if x < 4:
            if first_ryad[x - 1] == 0 or first_ryad[x - 1] == 2:
                print("Так нізя")
                return 1;
        elif x > 3 and x < 7:
            if second_ryad[x - 4] == 0 or second_ryad[x - 4] == 2:
                print("Так нізя")
                return 1;
        else:
            if third_ryad[x - 7] == 0 or third_ryad[x - 7] == 2:
                print("Так нізя")
                return 1;

    def perevirkaPeremogy():
        if first_ryad[0] == 0 and first_ryad[1] == 0 and first_ryad[2] == 0:
            print("Нулик переміг")
            return 1
        elif second_ryad[0] == 0 and second_ryad[1] == 0 and second_ryad[2] == 0:             
            print("Нулик переміг")
            return 1
        elif third_ryad[0] == 0 and third_ryad[1] == 0 and third_ryad[2] == 0:
            print("Нулик переміг")
            return 1
        elif first_ryad[0] == 0 and second_ryad[1] == 0 and third_ryad[2] == 0:
            print("Нулик переміг")
            return 1
        elif first_ryad[0] == 0 and second_ryad[0] == 0 and third_ryad[0] == 0:            
            print("Нулик переміг")
            return 1
        elif first_ryad[1] == 0 and second_ryad[1] == 0 and third_ryad[1] == 0:            
            print("Нулик переміг")
            return 1
        elif first_ryad[2] == 0 and second_ryad[2] == 0 and third_ryad[2] == 0:
            print("Нулик переміг")
            return 1
        elif first_ryad[2] == 0 and second_ryad[1] == 0 and third_ryad[0] == 0:
            print("Нулик переміг")
            return 1
        elif first_ryad[0] == 2 and first_ryad[1] == 2 and first_ryad[2] == 2:
            print("Хрестик переміг")
            return 1
        elif second_ryad[0] == 2 and second_ryad[1] == 2 and second_ryad[2] == 2:
            print("Хрестик переміг")
            return 1
        elif third_ryad[0] == 2 and third_ryad[1] == 2 and third_ryad[2] == 2:
            print("Хрестик переміг")
            return 1
        elif first_ryad[0] == 2 and second_ryad[1] == 2 and third_ryad[2] == 2:
            print("Хрестик переміг")
            return 1
        elif first_ryad[0] == 2 and second_ryad[0] == 2 and third_ryad[0] == 2:
            print("Хрестик переміг")
            return 1
        elif first_ryad[1] == 2 and second_ryad[1] == 2 and third_ryad[1] == 2:
            print("Хрестик переміг")
            return 1
        elif first_ryad[2] == 2 and second_ryad[2] == 2 and third_ryad[2] == 2:
            print("Хрестик переміг")
            return 1
        elif first_ryad[2] == 2 and second_ryad[1] == 2 and third_ryad[0] == 2:
            print("Хрестик переміг")
            return 1
        else:
            if first_ryad[0] != 1 and first_ryad[1] != 1 and first_ryad[2] != 1 and second_ryad[0] != 1 and second_ryad[1] != 1 and second_ryad[2] != 1 and third_ryad[0] != 1 and third_ryad[1] != 1 and third_ryad[2] != 1:
                   print("Нічия")
                   return 1
            else:
                   return 0
    def pokazat(x , y , z):
        if x[0] == 0:
            print("0 | " , end="")
        elif x[0] == 2:
            print("X | " , end="")
        else:
            print("  | " , end="")
        if x[1] == 0:
            print("0 | " , end="")
        elif x[1] == 2:
            print("X | " , end="")
        else:
            print("  | " , end="")
        if x[2] == 0:
            print("0")
        elif x[2] == 2:
            print("X")
        else:
            print("")

        if y[0] == 0:
            print("0 | " , end="")
        elif y[0] == 2:
            print("X | " , end="")
        else:
            print("  | " , end="")
        if y[1] == 0:
            print("0 | " , end="")
        elif y[1] == 2:
            print("X | " , end="")
        else:
            print("  | " , end="")
        if y[2] == 0:
            print("0")
        elif y[2] == 2:
            print("X")
        else:
            print("")
        if z[0] == 0:
            print("0 | " , end="")
        elif z[0] == 2:
            print("X | " , end="")
        else:
            print("  | " , end="")
        if z[1] == 0:
            print("0 | " , end="")
        elif z[1] == 2:
            print("X | " , end="")
        else:
            print("  | " , end="")
        if z[2] == 0:
            print("0")
        elif z[2] == 2:
            print("X")
        else:
            print("")

    print("Гра Хрестики-Нолики на двох")
    print("Вкажіть номер клітинки, де ви хочете поставити хрестик. Рахунок йде зліва зверху від 1 до 9 : ")
    while(1):
        if a == 0:
            pokazat(first_ryad, second_ryad, third_ryad)
            print("Вкажіть де ви хочете поставити хрестик")
            xCoordinate = int(input())
            if xCoordinate < 1 or xCoordinate > 9:
                print("Щось тут не так, повторіть")
                continue
            isProvirka = perevirka(xCoordinate)
            if isProvirka == 1:
                continue
            if xCoordinate == 1:
                first_ryad[0] = 2
            elif xCoordinate == 2:
                first_ryad[1] = 2
            elif xCoordinate == 3:
                first_ryad[2] = 2
            elif xCoordinate == 4:
                second_ryad[0] = 2
            elif xCoordinate == 5:
                second_ryad[1] = 2
            elif xCoordinate == 6:
                second_ryad[2] = 2
            elif xCoordinate == 7:
                third_ryad[0] = 2
            elif xCoordinate == 8:
                third_ryad[1] = 2
            elif xCoordinate == 9:
                third_ryad[2] = 2
        
            pobeda = perevirkaPeremogy()
            if pobeda == 1:
                pokazat(first_ryad, second_ryad, third_ryad)
                break
            a +=1
        elif a == 1:
            pokazat(first_ryad, second_ryad, third_ryad)
            print("Вкажіть де ви хочете поставити нолик")
            zeroCoordinate = int(input())
            if zeroCoordinate < 1 or zeroCoordinate > 9:
                print("Щось тут не так, повторіть")
                continue
            isProvirka = perevirka(zeroCoordinate)
            if isProvirka == 1:
                continue
            if zeroCoordinate == 1:
                first_ryad[0] = 0
            elif zeroCoordinate == 2:
                first_ryad[1] = 0
            elif zeroCoordinate == 3:
                first_ryad[2] = 0
            elif zeroCoordinate == 4:
                second_ryad[0] = 0
            elif zeroCoordinate == 5:
                second_ryad[1] = 0
            elif zeroCoordinate == 6:
                second_ryad[2] = 0
            elif zeroCoordinate == 7:
                third_ryad[0] = 0
            elif zeroCoordinate == 8:
                third_ryad[1] = 0
            elif zeroCoordinate == 9:
                third_ryad[2] = 0
            pobeda = perevirkaPeremogy()
            if pobeda == 1:
                pokazat(first_ryad, second_ryad, third_ryad)
                break
            a-=1
while(1):
    start_game = int(input('Для запуску гри "Хрестики-Нолики на двох" натисніть 0, для запуску гри "Вгадай число" натисніть 1, для виходу -1 : '))
    if start_game == 1:
        ugadai_chislo(1)
    elif start_game == 0:
        krestiki_noliki()
    elif start_game == -1:
        break
    else:
        print("Такої гри немає")
