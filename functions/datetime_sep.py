import re
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter
from colorama import Fore
import sys
import getpass
import time

def MyFunc(FILE, COLUMN1, COLUMN2, CHOOSE):
    # filename(Input)
    DATA = pd.read_csv(FILE, parse_dates=False)
    # Year
    if CHOOSE == '1':
        DATA[f'{COLUMN2}'] = pd.to_datetime(DATA[f'{COLUMN1}'], errors='coerce')
        DATA[f'{COLUMN2}'] = DATA[f'{COLUMN2}'].dt.year
    # Month
    if CHOOSE == '2':
        DATA[f'{COLUMN2}'] = pd.to_datetime(DATA[f'{COLUMN1}'], errors='coerce')
        DATA[f'{COLUMN2}'] = DATA[f'{COLUMN2}'].dt.month
    # Day
    if CHOOSE == '3':
        DATA[f'{COLUMN2}'] = pd.to_datetime(DATA[f'{COLUMN1}'], errors='coerce')
        DATA[f'{COLUMN2}'] = DATA[f'{COLUMN2}'].dt.day
    # Hour
    if CHOOSE == '4':
        DATA[f'{COLUMN2}'] = pd.to_datetime(DATA[f'{COLUMN1}'], errors='coerce')
        DATA[f'{COLUMN2}'] = DATA[f'{COLUMN2}'].dt.hour
    # filename(Input)
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
    # Column_1
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column Name(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER in df.columns:
            COLUMN1 = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")
    # Column_2
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column Name(Output)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

        COLUMN2 = USER
        break
    while True:
        # Options
        print(
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Year   -->  1\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Month  -->  2\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Day    -->  3\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Hour   -->  4\n"+
            "\n"
        )
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER in ['1', '2', '3', '4']:
            CHOOSE = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild Option, Try again")

    return FILE, COLUMN1, COLUMN2, CHOOSE

def Easy_Option():
    FILE, COLUMN1, COLUMN2, CHOOSE = USER_INPUT()
    MyFunc(FILE, COLUMN1, COLUMN2, CHOOSE)