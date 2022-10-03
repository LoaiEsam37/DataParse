import re
import pandas as pd
import os
from colorama import Fore
import sys
import getpass
import time

def MyFunc(FILE, COLUMN):

    # filename(Input)
    DATA = pd.read_csv(FILE, parse_dates=False)
    # Convert Column into DateTime
    DATA[f'{COLUMN}'] = pd.to_datetime(DATA[f'{COLUMN}'], dayfirst=True, errors='coerce')
    DATA.to_csv(FILE, index=False)

def USER_INPUT():

    # filename(Input)
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
    for i in df.columns:
        time.sleep(0.1)
        print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {i}")
    while True:
        # COLUMN
        print(f"{Fore.LIGHTGREEN_EX}Type Column Name(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER in df.columns:
            COLUMN = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")

    return FILE, COLUMN

def Easy_Option():
    FILE, COLUMN = USER_INPUT()
    MyFunc(FILE, COLUMN)