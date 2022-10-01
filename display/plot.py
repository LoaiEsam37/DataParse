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

def MyFunc1(FILE, COLUMN_X, label_X, label_Y, Title):
    all_data = pd.read_csv(FILE)
    plt.plot(all_data[f'{COLUMN_X}'], marker = 'o')
    plt.title(Title)
    plt.xlabel(label_X)
    plt.ylabel(label_Y)
    plt.show()

def MyFunc2(FILE, COLUMN_X, label_X, label_Y, Title):
    all_data = pd.read_json(FILE)
    plt.plot(all_data[f'{COLUMN_X}'], marker = 'o')
    plt.title(Title)
    plt.xlabel(label_X)
    plt.ylabel(label_Y)
    plt.show()

def USER_INPUT():

    print(
        "-----------------------------\n"+
        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} csv   -->  1\n"+
        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} json  -->  2\n"+
        "\n"+
        "-----------------------------\n"+
        "\n"
    )
    USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

    if USER == "1":
        func = "1"
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

        df = pd.read_csv(FILE)
        for i in df.columns:
            time.sleep(0.1)
            print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {i}")

        while True:
            print(f"{Fore.LIGHTGREEN_EX}Type Column Name(Input)")
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

            if USER in df.columns:
                COLUMN_X = USER
                break
            else:
                print(f"{Fore.RED}[ ! ] Invaild, Try again")        
    elif USER == "2":
        func = "2"
        COLUMN_X = "empty"
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
                    f = open(f"{os.getcwd()}/{USER}.json", "r")
                    f.close()
                    FILE = USER + ".json"
                    break
            except:
                print(f"{Fore.RED}[ ! ] invaild, Try again")
    else:
        print(f"{Fore.RED}[ ! ] Invaild, Try again")        
        
        df = pd.read_json(FILE)
        for i in df.columns:
            time.sleep(0.1)
            print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {i}")

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-X Name(Input)")
        label_X = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-Y Name(Input)")
        label_Y = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Title Name(Input)")
        Title = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break

    return FILE, COLUMN_X, label_X, label_Y, Title, func

def Easy_Option():
    FILE, COLUMN_X, label_X, label_Y, Title, func = USER_INPUT()
    if func == "1":
        MyFunc1(FILE, COLUMN_X, label_X, label_Y, Title)
    if func == "2":
        MyFunc2(FILE, COLUMN_X, label_X, label_Y, Title)