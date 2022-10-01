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

def MyFunc(DIR, OUTPUT):
    if DIR == "":
        path = os.getcwd()
    else:
        path = os.getcwd()+DIR
    # ls dir
    files = [file for file in os.listdir(path) if not file.startswith('.') and re.search(".csv", file) and not file == OUTPUT] # Ignore hidden files
    # declare dataframe
    all_months_data = pd.DataFrame()
    # concat files(Input)
    print("\n")
    for file in files:
        try:
            current_data = pd.read_csv(path+"/"+file)
            all_months_data = pd.concat([all_months_data, current_data])
            print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {file}")
        except:
            pass
    # open filename(output)
    all_months_data.to_csv(OUTPUT, index=False)

def USER_INPUT():

    # directory(Input)
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Directory(Input)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        try:
            DIR = os.path.join("/", USER)
            test = os.getcwd()+DIR
            os.listdir(test)
            break
        except:
            print(f"{Fore.RED}[ ! ] invaild, Try again")
    # filename(Output)
    while True:
        print(f"{Fore.LIGHTGREEN_EX}filename(Output)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        # CSV
        try:
            if re.search(".csv", USER):
                f = open(f"{os.getcwd()}/{USER}", "a")
                OUTPUT = USER
                break
            else:
                f = open(f"{os.getcwd()}/{USER}.csv", "a")
                OUTPUT = USER + ".csv"
                break
        except:
            print(f"{Fore.RED}[ ! ] invaild, Try again")

    return DIR, OUTPUT

def Easy_Option():
    DIR, OUTPUT = USER_INPUT()
    MyFunc(DIR, OUTPUT)
