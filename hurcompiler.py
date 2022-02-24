from colorama import Fore, init, Back
import sys
import os
import time
import math

#GLOBAL VARIABLE DECLARATION
global NO_COLOR
NO_COLOR = False

#CUSTOM ERROR FUNCTION
def error(code):
    if not int(code):
        print("Bad error usage!")
        exit()
    else:
        code = int(code)
    if code == 0:
        print("Unexpected error! [0]")
        exit()
    elif code == 1:
        print(f"[1] Error! Execute {Fore.YELLOW}{sys.argv[0]} --help{Fore.RESET}")
        exit()

#CLEAR SCREEN FUNCTION
def cls():
    os.system("cls" if os.name == "nt" else "clear")

#CHECK IF NO ARGUMENTS
if len(sys.argv) < 2:
    error(1)

#DEFINE ARGUMENTS
def define_arguments():
    if "--no-color" in sys.argv or "-nc":
        NO_COLOR = True

if NO_COLOR == False:
    init()


#BANNER
def banner():
    if NO_COLOR:
        print("""
-----------------------------------------
HURSCRIPT - SEMIAUTOMATIC HACKING SCRIPT
-----------------------------------------
""")
    else:
        print(f"""
{Fore.RED}-----------------------------------------{Fore.RESET}
{Fore.YELLOW}HURSCRIPT - SEMIAUTOMATIC HACKING SCRIPT{Fore.RESET}
{Fore.RED}-----------------------------------------{Fore.RESET}
""")

cls()
banner()
