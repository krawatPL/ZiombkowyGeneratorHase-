import random
import os
import time
import keyboard
import math

keyboard.press('f11')

with open("UzywaneZnaki.txt", "r") as file:
    characters = file.read().strip()


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




# sposob na zamienianie literek na cyfry podjebalem z stack overflow 
# https://stackoverflow.com/questions/2449848/how-to-make-a-variable-change-from-the-text-1m-into-1000000-in-python
# a pozniej wjebalem do chatu gpt bo mi sie myslec nie chcialo xd i chyba dziala

# ten sciek w komentarzu ponizej to ten pseudooryginalny kod

# number_of_passwords = str(input("Ile haseł generujemy?: "))
#tens = {'k': 1e3, 'm': 1e6, 'b': 1e9}
#f = lambda x: int(float(x[:-1])*tens[x[-1]])
#number_of_passwords = f(number_of_passwords)


def parse_input(input_str):
    tens = {'k': 1e3, 'm': 1e6, 'b': 1e9}
    if input_str[-1].lower() in tens:
        return int(float(input_str[:-1].replace(',', '.')) * tens[input_str[-1].lower()])
    else:
        try:
            return int(input_str.replace(',', '.'))
        except ValueError:
            return None

while True:
    number_of_passwords = input("Ile haseł generujemy?: ")
    number_of_passwords = parse_input(number_of_passwords)

    if number_of_passwords is None or number_of_passwords <= 0:
        print("Podano nieprawidłową liczbę haseł.")
    else:
        break  # Przerwij pętlę, gdy użytkownik poda poprawną wartość

    
    
    

    
def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(eval(user_input))
            if value <= 0:
                print("Podana wartość musi być liczbą całkowitą dodatnią.")
                continue
            return value
        except Exception:
            print("Nieprawidłowe dane. Wprowadź poprawną liczbę całkowitą.")


while True:
    password_length1 = get_valid_input("Długość haseł od: ")
    password_length2 = get_valid_input("Długość haseł do: ")

    if password_length2 < password_length1:
        print("Druga liczba musi być większa od pierwszej.")
    else:
        break



filename = "testowanie_predkosci_zapisu.txt"
predkosci = []

for batch_index in range(100000 // 1000):
    start_time = time.time() 
    passwords_to_write = []
    for _ in range(1000):
        final_password = ''.join(random.choice(characters) for _ in range(random.randint(password_length1, password_length2)))
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

# chciałem się zakurwić jak to pisałem, szukałem błedu itp, a poprostu zamiast wpisać:
# if number_of_passwords < int(math.trunc(srednia_predkosc)):
# wpisałem kurwa
# batch_size < int(math.trunc(srednia_predkosc)):
batch_size = int(zk_predkosc)
if number_of_passwords < int(math.trunc(srednia_predkosc)):
   batch_size = number_of_passwords
# batch_size = int(input(f"Wielkość jednej części (optymalna {fr_predkosc}): "))


def wybrane_ustawienia():
    print("\n---------------------------------------------------------------------\n")
    print("                  \\/ WYBRANE USTAWIENIA \\/                           \n")
    print("Generowanie " + str(format(number_of_passwords, ',d')) + " losowych haseł.")
    print("Wielkość jednej części wynosi (wyliczona automatycznie): " + str(format(batch_size, ',d')) + ".")
    print(("Dlugosc hasel: " + str(password_length1) + " - " + str(password_length2)))
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
        final_password = ''.join(random.choice(characters) for _ in range(random.randint(password_length1, password_length2)))
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
print(f"Dlugosc haseł ~ " + str(password_length1) + " - " + str(password_length2))
print(f"Cała operacja zajęła ~ {format(godziny2, ",.1f")}h, {format(minuty2, ",.1f")}m, {format(sekundy2, ",.3f")}s")
print("\n---------------------------------------------------------------------\n")
input("Naciśnij Enter, aby zakończyć")
