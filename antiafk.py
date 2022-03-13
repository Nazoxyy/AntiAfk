import pyautogui 
import os
import time
from pystyle import Colors, Colorate

clear = lambda: os.system('cls')

def main():
    print(Colorate.Vertical(Colors.purple_to_blue, antiafk, 1))
    a = input(" \n\n\n [!] Start [Y/N] --> ")                                                      
    if a == 'Y':
        valo()
    else:
        exit()   

def valo():
    clear()

    print(Colorate.Vertical(Colors.purple_to_blue, antiafk, 1))
    print("\n\n\n [!] Début dans 10seconde veullez mettre votre jeux en pleine ecrann, cliquer sur z pour stoper l'antiafk")
    time.sleep(10)
    pyautogui.keyDown('Z')
    input("\n\nENTER POUR RETOURNER SUR LE MENU")

antiafk = '''                   
                      /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$        /$$$$$$  /$$$$$$$$ /$$   /$$
                     /$$__  $$| $$$ | $$|__  $$__/|_  $$_/       /$$__  $$| $$_____/| $$  /$$/
                    | $$  \ $$| $$$$| $$   | $$     | $$        | $$  \ $$| $$      | $$ /$$/ 
                    | $$$$$$$$| $$ $$ $$   | $$     | $$        | $$$$$$$$| $$$$$   | $$$$$/  
                    | $$__  $$| $$  $$$$   | $$     | $$        | $$__  $$| $$__/   | $$  $$  
                    | $$  | $$| $$\  $$$   | $$     | $$        | $$  | $$| $$      | $$\  $$ 
                    | $$  | $$| $$ \  $$   | $$    /$$$$$$      | $$  | $$| $$      | $$ \  $$
                    |__/  |__/|__/  \__/   |__/   |______/      |__/  |__/|__/      |__/  \__/'''

if __name__ == "__main__":
    while True:
        clear()
        main()