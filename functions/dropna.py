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

def MyFunc(FILE):
    DATA = pd.read_csv(FILE)
    nan_df = DATA[DATA.isna().any(axis=1)]
    NaN = len(re.findall("NaN", nan_df.to_string()))
    print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {NaN} were Found")
    DATA = DATA.dropna(how="all")
    DATA.to_csv(FILE, index=False)

def USER_INPUT():
    # FILE
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type filename(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

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

    return FILE

def Easy_Option():
    FILE = USER_INPUT()
    MyFunc(FILE)