#|-----------------------|
#|   Name: hermes        |
#|   Author: Lawliet     |
#|   Version: 0.1        |
#|-----------------------|

import argparse
from termcolor import cprint, colored

print('')
A = '''
     _   _   _____   ____    __  __   _____   ____  
    | | | | | ____| |  _ \\  |  \\/  | | ____| / ___| 
    | |_| | |  _|   | |_) | | |\\/| | |  _|   \\___ \\ 
    |  _  | | |___  |  _ <  | |  | | | |___   ___) |
    |_| |_| |_____| |_| \\_\\ |_|  |_| |_____| |____/ 
    
        Hermes dork scanner (V0.1) coded by Lawliet
        To use type: python3 hermes.py -n
        To see more parameters use: python3 hermes.py -h | --help
    '''
cprint(A, 'magenta')
print('')

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--normal", help = "Use the normal mode", action = 'store_true')
args =  parser.parse_args()

if args.normal:
    from search import normal_mode
