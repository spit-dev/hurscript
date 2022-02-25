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
        if NO_COLOR == False:
            print(f"[1] Error! Execute {Fore.YELLOW}{sys.argv[0]} --help{Fore.RESET}")
            exit()
        else:
            print(f"[1] Error! Execute --help")
            exit()
    elif code == 2:
        print(f"[2] Error! Invalid input file")
        exit()
    elif code == 3:
        print(f"[3] Error! Unaccesible input file")
        exit()

#CLEAR SCREEN FUNCTION
def cls():
    os.system("cls" if os.name == "nt" else "clear")

#CHECK IF NO ARGUMENTS
if len(sys.argv) < 2:
    error(1)

#DEFINE ARGUMENTS
if "--no-color" in sys.argv or "-nc" in sys.argv:
        NO_COLOR = True
try:
    inp_filename = sys.argv[int(sys.argv.index("-i"))+1]
    print(inp_filename)
except:
    error(2)

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

def loadfile():
    print("[LOG] Reading...")
    print(f"[LOG] Input filename: \"{inp_filename}\"")
    try:
        print("[LOG] Trying to open file...")
        t_file = open(f"{inp_filename}", "rb")
        t_file.close()
        print("[LOG] File loaded correctly...")
    except:
        error(3)

def fetchcommands():
    try:
        m_file = open(f"{inp_filename}", "r")
        m_lines = m_file.readlines()
        for n in range(len(m_lines)):
            m_lines[n] = str(m_lines[n])[:-1]
        print(m_lines)
    except:
        print()

cls()
banner()
loadfile()
fetchcommands()
