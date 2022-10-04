import re
import pandas as pd
import os
from colorama import Fore
import sys
import getpass
import time

def MyFunc(FILE, ROW):

    # filename(Input)
    dataFrame = pd.read_csv(FILE)
    # Drop the row
    dataFrame = dataFrame.drop(ROW, axis=0)
    # filename(Output)
    dataFrame.to_csv(FILE, index = False)
    print(f"{Fore.RED}-{Fore.WHITE} {ROW}")

def USER_INPUT():
    # FILE
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type filename(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        # CSV
        try:
            try:
                f = open(f"{os.getcwd()}/{USER}", "r")
                f.close()
                FILE = USER
                break
            except:
                f = open(f"{os.getcwd()}/{USER}.csv", "r")
                f.close()
                FILE = USER + ".csv"
                break
        except:
            print(f"{Fore.RED}[ ! ] invaild, Try again")
    # filename(Input)
    df = pd.read_csv(FILE)
    print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {df.index[-1]}")
    # ROW
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Row Number(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        try:
            USER = int(USER)
            if 0 < USER < df.index[-1]:
                ROW = USER
                break
            else:
                print(f"{Fore.RED}[ ! ] Invaild, Try again")
        except:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")
    return FILE, ROW

def Easy_Option():
    FILE, ROW = USER_INPUT()
    MyFunc(FILE, ROW)