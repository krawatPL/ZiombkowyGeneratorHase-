import random
import os
import time

characters = 'abcdefghijklmnopqrstuvwxyz'

os.system('cls')
os.system('color a')

def pisz(passwords, filename):
    with open(filename, "a") as file:
        for final_password in passwords:
            file.write(final_password + "\n")

napis = '''
  _____  _                       _              _             _                 _ 
 |__  / (_)   ___    _ __ ___   | |__     ___  | | __   ___  | |__    _   _    (_)
   / /  | |  / _ \  | '_ ` _ \  | '_ \   / _ \ | |/ /  / __| | '_ \  | | | |   | |
  / /_  | | | (_) | | | | | | | | |_) | |  __/ |   <  | (__  | | | | | |_| |   | |
 /____| |_|  \___/  |_| |_| |_| |_.__/   \___| |_|\_\  \___| |_| |_|  \__,_|  _/ |
                                                                             |__/ 
'''

napis2 = '''
   __ _              _                                 
  / _` |    ___     | |_      ___    __ __ __    ___   
  \__, |   / _ \    |  _|    / _ \   \ V  V /   / -_)  
  |___/    \___/    _\__|    \___/    \_/\_/    \___|  
_|"""""| _|"""""| _|"""""| _|"""""| _|"""""|  _|"""""| 
"`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-' "`-0-0-'  "`-0-0-' 
'''

print(napis)

number_of_passwords = int(input("Ile haseł generujemy?: "))
password_length = int(input("Jaką długość mają mieć hasła?: "))

filename = "testowanie_predkosci_zapisu.txt"
predkosci = []

for batch_index in range(50000 // 1000):
    start_time = time.time() 
    passwords_to_write = []
    for _ in range(1000):
        final_password = ''.join(random.choice(characters) for _ in range(password_length))
        passwords_to_write.append(final_password)
    pisz(passwords_to_write, filename)
    end_time = time.time() 
    duration = end_time - start_time 
    predkosc = 1000 / duration
    predkosci.append(predkosc)

srednia_predkosc = sum(predkosci) / len(predkosci)

os.remove("testowanie_predkosci_zapisu.txt")


zk_predkosc = round(srednia_predkosc, 2)

fr_predkosc = "{:,.2f}".format(zk_predkosc)


batch_size = int(input(f"Wielkość jednej części (optymalna {fr_predkosc}): "))



def wybrane_ustawienia():
    print("\n---------------------------------------------------------------------\n")
    print("                  \\/ WYBRANE USTAWIENIA \\/                           \n")
    print("Generowanie " + str(format(number_of_passwords, ',d')) + " losowych haseł.")
    print("Wielkość jednej części wynosi: " + str(format(batch_size, ',d')) + ".")
    print("Długość haseł: " + str(password_length))
    print("---------------------------------------------------------------------\n")

wybrane_ustawienia()

start_time_cala_operacja = time.time()

filename = "giganiga.txt"
predkosci = []

wykonane_operacje = 0

for batch_index in range(number_of_passwords // batch_size):
    start_time = time.time() 
    passwords_to_write = []
    for _ in range(batch_size):
        final_password = ''.join(random.choice(characters) for _ in range(password_length))
        passwords_to_write.append(final_password)
    pisz(passwords_to_write, filename)
    end_time = time.time() 
    duration = end_time - start_time 
    predkosc = batch_size / (duration + 0.000000000000001)
    ile_scieku_zostalo = number_of_passwords - ((batch_index + 1) * batch_size)
    predkosci.append(predkosc)
    srednia_predkosc = sum(predkosci) / len(predkosci)
    eta = ile_scieku_zostalo / round(srednia_predkosc, 2)
    godziny = eta // 3600
    reszta = eta % 3600
    minuty = reszta // 60
    sekundy = reszta % 60
    print(f'Część {batch_index + 1} / {format(round(number_of_passwords / batch_size), ",")} | { format(round((batch_index + 1) / (number_of_passwords / batch_size) * 100, 2), '.2f')}% | Prędkość: {format(predkosc, ",.2f")}/s | Pozostało: {format(godziny, ",.1f")}h, {format(minuty, ",.1f")}m, {format(sekundy, ",.1f")}s')

end_time_cala_operacja = time.time() 
duration_cala_operacja = end_time_cala_operacja - start_time_cala_operacja
godziny2 = duration_cala_operacja // 3600
reszta2 = duration_cala_operacja % 3600
minuty2 = reszta2 // 60
sekundy2 = reszta2 % 60


print(napis2)


print("\n---------------------------------------------------------------------")
print("\n                           [ Statystyki ]\n")
print(f"Wygenerowano ~ {format(int(number_of_passwords), ',d')}")
print(f"Średnia prędkość generacji ~ {format(srednia_predkosc, ",.2f")} haseł / s")
print("Wielkość jednej części wynosiła ~ " + str(format(batch_size, ',d')))
print(f"Długość generowanych haseł ~ {password_length}")
print(f"Cała operacja zajęła ~ {format(godziny2, ",.1f")}h, {format(minuty2, ",.1f")}m, {format(sekundy2, ",.3f")}s")
print("\n---------------------------------------------------------------------\n")
input("Naciśnij Enter, aby zakończyć")
