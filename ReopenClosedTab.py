# Author MAVERICK
import json
import psutil
import time
import subprocess
import os,colorama
from tabulate import tabulate
from string import ascii_lowercase
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#os.system('mode con: cols=80 lines=30')

#========================================

RED =  F"{Fore.RED}"
GREEN =  F"{Fore.GREEN}"
YELLOW = F"{Fore.YELLOW}"
BLUE = F"{Fore.BLUE}"
MAGENTA = F"{Fore.MAGENTA}"
CYAN = F"{Fore.CYAN}"
WHITE =  F"{Fore.WHITE}"

LRED =  F"{Fore.LIGHTRED_EX}"
LGREEN =  F"{Fore.LIGHTGREEN_EX}"
LYELLOW = F"{Fore.LIGHTYELLOW_EX}"
LBLUE = F"{Fore.LIGHTBLUE_EX}"
LMAGENTA = F"{Fore.LIGHTMAGENTA_EX}"
LCYAN = F"{Fore.LIGHTCYAN_EX}"
LWHITE = F"{Fore.LIGHTWHITE_EX}"

#========================================

#print(f'{Fore.LIGHTYELLOW_EX}{tabulate(table, showindex="always", tablefmt="fancy_grid", stralign="left", numalign="left")}')

#time.sleep(5)
#pyautogui.write("10310337")
#pyautogui.press('enter')

#if a in ascii_lowercase:

flag = False
listOfRunningProcessNames = []
listOfRunningProcessPID = []

defaultPrograms = [
                        "csrss.exe",
                        "explorer.exe",
                        "lsass.exe",
                        "mstask.exe",
                        "services.exe",
                        "smss.exe",
                        "spoolsv.exe",
                        "svchost.exe",
                        "python.exe",
                        "systemsettings.exe",
                        "applicationframeHost.exe",
                        "binance.exe",
                        ]
onOff = {}
logDirectory = ".\\logs.json"


def getInstalledProgramList():
    psutil.process_iter(attrs=None, ad_value=None)
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = proc.pid
            if processName in defaultPrograms : pass
            else:
                if processName in listOfRunningProcessNames or processName.lower() in listOfRunningProcessNames: pass
                else :
                    listOfRunningProcessNames.append(processName)
                    listOfRunningProcessPID.append(processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def convertIdToPath(x):
    p = psutil.Process(x)
    return p.exe()

def repeat():
    onOff.clear()
    for number in listOfRunningProcessPID:
        try:
            path = convertIdToPath(number)
            onOff[path] = 0
        except (AttributeError,PermissionError,psutil.AccessDenied,psutil.NoSuchProcess,ProcessLookupError): pass
    with open(logDirectory,"w") as f: f.write(json.dumps(onOff, indent=4, sort_keys=True))



def initialPrompt():
    print(f"{LGREEN}Restore all previous sessions ? {LCYAN}Y / {LMAGENTA}N = ", end="")
    x = input()
    if x == "N" or x == "n":
        main()
    elif x == "Y" or x == "y":
        with open(logDirectory, "r+") as f: d = json.load(f)
        for k,v in d.items():
            print(k)
            os.system(f'"{k}"')



def main():
    getInstalledProgramList()
    repeat() # add programs at definite interval
    for k,v in onOff.items(): print(k,v)
    #time.sleep(30)
    #main()
    
    
initialPrompt()

if __name__ == "__main__": main()







