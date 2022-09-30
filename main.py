#!/usr/bin/python3
import re
import os
from colorama import Fore
import sys
import getpass
# Import files Project

import functions.concat as CONCAT
import functions.dropna as DROPNA
import functions.dropgroup as DROPCOLUMN
import functions.droprow as DROPROW
import functions.dropduplicates as DROPDUPLICATES
import functions.datetime as DATETIME
import functions.int as INT
import functions.datetime_sep as DATETIME_SEP

import mathmatics_functions.statics as STATICS
import mathmatics_functions.multiply as MULTIPLY
import mathmatics_functions.minus as MINUS
import mathmatics_functions.divide as DIVIDE

def DEFAULT():
    print(
        Fore.LIGHTGREEN_EX+
    " ____        _        ____                      \n"+
    "|  _ \  __ _| |_ __ _|  _ \ __ _ _ __ ___  ___ \n"+
    "| | | |/ _` | __/ _` | |_) / _` | '__/ __|/ _ \\\n"+
    "| |_| | (_| | || (_| |  __/ (_| | |  \__ \  __/\n"+
    "|____/ \__,_|\__\__,_|_|   \__,_|_|  |___/\___|\n"
    )

    while True:
        print(
            Fore.WHITE+
            f"-----------------------------\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Functions    -->  1\n"+
            f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} MathMatics   -->  2\n"+
            f"\n"+
            f"-----------------------------"+
            f"\n"
        )
        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")


        if USER == "1":
            # Functions
            while True:
            
                print(
                    "\n"
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ConCat             -->  1\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropNA             -->  2\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropColumn         -->  3\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropRow            -->  4\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} DropDuplicates     -->  5\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ConvertToDateTime  -->  6\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ConvertToInt       -->  7\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} ExtractDate        -->  8\n"+
                    f"\n"+
                    f"-----------------------------"+
                    f"\n"
                )

                USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")                

                if USER == '1':
                    print(f"{Fore.WHITE}[ OK ] ConCat Selected")
                    CONCAT.Easy_Option()
                    break
                elif USER == '2':
                    print(f"{Fore.WHITE}[ OK ] DropNA Selected")
                    DROPNA.Easy_Option()
                    break
                elif USER == '3':
                    print(f"{Fore.WHITE}[ OK ] DropColumn Selected")
                    DROPCOLUMN.Easy_Option()
                    break
                elif USER == '4':
                    print(f"{Fore.WHITE}[ OK ] DropRow Selected")
                    DROPROW.Easy_Option()
                    break
                elif USER == '5':
                    print(f"{Fore.WHITE}[ OK ] DropDuplicates Selected")
                    DROPDUPLICATES.Easy_Option()
                    break
                elif USER == '6':
                    print(f"{Fore.WHITE}[ OK ] ConvertToDateTime")
                    DATETIME.Easy_Option()
                    break
                elif USER == '7':
                    print(f"{Fore.WHITE}[ OK ] ConvertToInt")
                    INT.Easy_Option()
                    break
                elif USER == '8':
                    print(f"{Fore.WHITE}[ OK ] ExtractDate")
                    DATETIME_SEP.Easy_Option()
                    break
                else:
                    print(f"{Fore.RED}[ ! ] Invaild Option, Try again")

        elif USER == "2":
            # MathMatics
            while True:

                print(
                    "\n"
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Statics     -->  1\n"+
                    f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Operations  -->  2\n"+
                    f"\n"+
                    f"-----------------------------"+
                    f"\n"
                )
            
                USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

                if USER == '1':
                    print(f"{Fore.WHITE}[ OK ] Statics Selected")
                    STATICS.Easy_Option()
                    break    

                elif USER == '2':
                    while True:
                        print(
                        "\n"
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Sum        -->  1\n"+
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Minus      -->  2\n"+
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Multiply   -->  3\n"+
                        f"{Fore.LIGHTGREEN_EX}+{Fore.WHITE} Divide     -->  4\n"+
                        f"\n"+
                        f"-----------------------------"+
                        f"\n"
                    )

                        USER = input(f"{Fore.WHITE}{getpass.getuser()}@DataParse$ ")

                        if USER == "1":
                            print(f"{Fore.WHITE}[ OK ] Sum Selected")
                            SUM.Easy_Option()
                            break
                        elif USER == "2":
                            print(f"{Fore.WHITE}[ OK ] Minus Selected")
                            MINUS.Easy_Option()
                            break
                        elif USER == "3":
                            print(f"{Fore.WHITE}[ OK ] Multiply Selected")
                            MULTIPLY.Easy_Option()
                            break
                        elif USER == "4":
                            print(f"{Fore.WHITE}[ OK ] Divide Selected")
                            DIVIDE.Easy_Option()
                            break
                        else:
                            print(f"{Fore.RED}[ ! ] Invaild Option, Try again")
                    break
                else:
                    print(f"{Fore.RED}[ ! ] Invaild Option, Try again")

        else:
            print(f"{Fore.RED}[ ! ] Invaild Option, Try again")
DEFAULT()
