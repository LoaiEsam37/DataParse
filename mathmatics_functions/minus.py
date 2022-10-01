import re
import pandas as pd
import numpy as np
import os
from colorama import Fore
import sys
import getpass
import time

def MyFunc(FILE, COLUMN1, COLUMN2, RES, df):
    # filename(Input)
    all_data = pd.read_csv(FILE)
    # minus
    all_data[f'{RES}'] = all_data[f'{COLUMN1}'] - all_data[f'{COLUMN2}']
    # filename(Output)
    all_data.to_csv(FILE, index=False)

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
    # COLUMN1
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column1 Name(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER in df.columns:
            COLUMN1 = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")
    # COLUMN2
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column2 Name(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER in df.columns:
            COLUMN2 = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")
    # OUTPUT COLUMN
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column Name(Output)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        RES = USER
        break

    return FILE, COLUMN1, COLUMN2, RES, df

def Easy_Option():
    FILE, COLUMN1, COLUMN2, RES, df = USER_INPUT()
    MyFunc(FILE, COLUMN1, COLUMN2, RES, df)