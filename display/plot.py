import pandas as pd
import os
import matplotlib.pyplot as plt
from colorama import Fore
import numpy as np
import getpass
import time
import json

def MyFunc1(FILE, COLUMN_X, label_X, label_Y, Title):
    # filename(Input)
    all_data = pd.read_csv(FILE)
    # plot
    plt.plot(all_data[f'{COLUMN_X}'], marker = 'o')
    # Title
    plt.title(Title)
    # Labels
    plt.xlabel(label_X)
    plt.ylabel(label_Y)
    # show
    plt.show()

def MyFunc2(FILE, COLUMN_X, label_X, label_Y, Title, SCATTER, LINEAR, POLY):
    # filename (Input)
    with open(FILE, "r") as read_file:
        data = json.load(read_file)
        
    x = data['x']
    y = data['y']
    try:
        model = data['model']
    except:
        pass
    if SCATTER:
        plt.bar(x, y)
    if POLY:
        try:
            model = np.poly1d(np.polyfit(x, y, 3))
            line = np.linspace(1, len(x), 100)
            plt.plot(line, model(line))
        except Exception as e:
            exit(e)
    if LINEAR:
        try:
            plt.plot(x, model)
        except Exception as e:
            exit(e)
    # Title
    plt.title(Title)
    # Labels
    plt.xlabel(label_X)
    plt.ylabel(label_Y)
    # show
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
        # filename(Input)
        while True:
            print(f"{Fore.LIGHTGREEN_EX}Type filename(Input)")
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
            # JSON
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
        # filename(Input)
        df = pd.read_json(FILE)
        for i in df.columns:
            time.sleep(0.1)
            print(f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} {i}")
    # Label-X
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-X Name(Input)")
        label_X = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break
    # Label-Y
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type label-Y Name(Input)")
        label_Y = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break
    # Title
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Type Title Name(Input)")
        Title = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        break

    while True:
        print(f"{Fore.LIGHTGREEN_EX}Do you want to display original data (yes  -->  1, No  -->  2)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER == "1":
            SCATTER = True
            break
        elif USER == "2":
            SCATTER = False
            break
        else:
            print(f"{Fore.RED}[ ! ] invaild, Try again")
        
    while True:
        print(f"{Fore.LIGHTGREEN_EX}Is it Polynomial (yes  -->  1, No  -->  2)")
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
        if USER == "1":
            POLY = True
            break
        elif USER == "2":
            POLY = False
            break
        else:
            print(f"{Fore.RED}[ ! ] invaild, Try again")
        
    if not POLY:
        while True:
            print(f"{Fore.LIGHTGREEN_EX}Is it Linear (yes  -->  1, No  -->  2)")
            USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")
            if USER == "1":
                LINEAR = True
                break
            elif USER == "2":
                LINEAR = False
                break
            else:
                print(f"{Fore.RED}[ ! ] invaild, Try again")

    else:
        LINEAR = False
    return FILE, COLUMN_X, label_X, label_Y, Title, func, SCATTER, LINEAR, POLY

def Easy_Option():
    FILE, COLUMN_X, label_X, label_Y, Title, func, SCATTER, LINEAR, POLY = USER_INPUT()
    if func == "1":
        MyFunc1(FILE, COLUMN_X, label_X, label_Y, Title)
    if func == "2":
        MyFunc2(FILE, COLUMN_X, label_X, label_Y, Title, SCATTER, LINEAR, POLY)