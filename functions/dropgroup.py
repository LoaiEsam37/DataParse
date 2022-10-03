import re
import pandas as pd
import os
from colorama import Fore
import sys
import getpass
import time

def MyFunc(FILE, COLUMN, df):

    # filename(Input)
    dataFrame = pd.read_csv(FILE)
    # drop the column
    dataFrame = dataFrame.drop([f'{COLUMN}'], axis = 1)
    # filename(Output)
    dataFrame.to_csv(FILE, index = False)
    for i in df.columns:
        time.sleep(0.1)
        if i == COLUMN:
            print(f"{Fore.RED}-{Fore.WHITE} {i}")
        else:
            print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {i}")

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
    # COLUMN
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Column(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER in df.columns:
            COLUMN = USER
            break
        else:
            print(f"{Fore.RED}[ ! ] Invaild, Try again")

    return FILE, COLUMN, df

def Easy_Option():
    FILE, COLUMN, df = USER_INPUT()
    MyFunc(FILE, COLUMN, df)