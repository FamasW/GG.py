#!/usr/bin/python3
import os
import time
import webbrowser

senha = int(input("Digite a senha: "))
if senha == 6845:
    print("Senha correta!")
else:
    print("Senha incorreta!")
    os.system("clear")
    os.system("exit")
    print ("")
    
os.system("clear")
print("LOADING...")
time.sleep(2)
os.system("clear")
os.system("sl")
time.sleep(3)


os.system("cd /storage/emulated/0/NEW-TEAM/") 
print("█▀▄▀█ █▀▀ █▄░█ █░█")
print("█░▀░█ ██▄ █░▀█ █▄█")

print("█▀▀ █▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄ █▀█ █▀")
print("█▄▄ █▄█ █░▀░█ █▀█ █░▀█ █▄▀ █▄█ ▄█")
print("")

print ("1: SERVIDOR APK")
print ("2: DIALOG ONLINE")
print ("3: MANUTENÇÃO-CRASH")
print ("4: CLEAR LINHAS")
print ("5: PAINEL OFF")
print ("     ")

escolha = False

while escolha == False:
    nivel = int(input("QUAL OPÇÃO: "))
    
    if (nivel == 1):
        os.system("nano servidor-apk.json")
    
    elif (nivel == 2):
        os.system("nano dialog-online.json")
    
    elif (nivel == 3):
        os.system("nano manutenção-crash.json")
    elif (nivel == 4):
        os.system("clear")
    
    elif (nivel == 5):
        os.system("exit")