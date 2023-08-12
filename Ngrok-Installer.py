import os
import sys
import time
from time import sleep

#file coded by IRSYAD'S

os.system("clear")
print("=================================PROCESSING=================================")
os.system("apt update -y")
os.system("apt upgrade -y")
print("============================================================================")
sleep(3)
os.system("clear")
print("Login dulu,baru lanjut")
sleep(2)
os.system("clear")
print("====================================LOGIN===================================")
a = "Login dengan akun anda"
print(a)
sleep(3)
b2 = "termux-open-url https://dashboard.ngrok.com/signup"
os.system(b2)
sleep(5)
print("Sesudah Login lanjut ke step berikutnya...")
os.system("clear")
print("============================================================================")
sleep(10)
os.system("clear")
os.system("figlet OK Bang")
sleep(3)
os.system("clear")

print("=================================DOWNLOADING================================")
url_untuk_wget = "wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.tgz"
os.system(url_untuk_wget)
print("============================================================================")
sleep(2)
print("|")
print("=================================EXTRACTING=================================")
extract = "tar -xvf ngrok-v3-stable-linux-arm.tgz"
os.system(extract)
print("============================================================================")
sleep(3)
print("|")

print("=================================PROCESSING=================================")
print(" *Exaple: ./ngrok config add-authtoken 2OVZ****************************_****")
authtoken = input("Insert Ngrok Config = ")
os.system(authtoken)
print("============================================================================")
print("Laman ini akan ditutup dalam 5 detik.....")
sleep(5)
os.system("clear")