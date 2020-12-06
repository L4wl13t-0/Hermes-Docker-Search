#|-----------------------|
#|   Name: hermes        |
#|   Author: Lawliet     |
#|   Version: 0.1        |
#|-----------------------|

from googlesearch import search
import random
import sys, os
from termcolor import colored, cprint

def clear(): 
    return os.system('cls' if os.name == 'nt' else 'clear')

clear()

print('')
A = '''
     _   _   _____   ____    __  __   _____   ____  
    | | | | | ____| |  _ \\  |  \\/  | | ____| / ___| 
    | |_| | |  _|   | |_) | | |\\/| | |  _|   \\___ \\ 
    |  _  | | |___  |  _ <  | |  | | | |___   ___) |
    |_| |_| |_____| |_| \\_\\ |_|  |_| |_____| |____/ 
    
        Hermes dork scanner (V0.1) coded by Lawliet
   
    '''
cprint(A, 'magenta')
print('')

domain = ["com", "com.tw", "co.in", "be", "de", "co.uk", "co.ma", "dz", "ru", "ca", "es"]
dork = input(colored("[-] Please set a dork: ", 'white'))
resultn = int(input(colored("[-] Please set a number for results: ", 'white')))
tld = random.choice(domain)
cprint("\n[-] Searching pages...", 'green')

for page in search(dork, tld = tld, num = resultn, start = 0, stop = 150, pause = 2):
    print(colored("[*] Found: ", 'green') + page)