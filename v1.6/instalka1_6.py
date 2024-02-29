import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

print("instaluje modul 'keyboard'...")
install('keyboard')
print("\ninstaluje modul 'requests'...")
install('requests')
import requests

print("\nPobieram plik wykonywalny...")
r = requests.get("https://github.com/krawatPL/ZiombkowyGeneratorHase-/raw/main/v1.6/zg1_6.exe", allow_redirects=True)
open('zg1_6.exe', 'wb').write(r.content)

print("\nPobieram Adnotacja.txt...")
r = requests.get("https://github.com/krawatPL/ZiombkowyGeneratorHase-/raw/main/v1.6/v1.6%20Dodatkowe%20pliki/Adnotacja.txt", allow_redirects=True)
open('Adnotacja.txt', 'wb').write(r.content)

print("\nPobieram UzywaneZnaki.txt...")
r = requests.get("https://github.com/krawatPL/ZiombkowyGeneratorHase-/raw/main/v1.6/v1.6%20Dodatkowe%20pliki/UzywaneZnaki.txt", allow_redirects=True)
open('UzywaneZnaki.txt', 'wb').write(r.content)

print("\n\n\n\n\n\n\nGOTOWE, przeczytaj Adnotacja.txt po więcej informacji\n(ten plik można bezpiecznie usunąć)")

input("\n\n\n\n\nNaciśnij Enter, aby zakończyć")