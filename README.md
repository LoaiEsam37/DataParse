# DataParse

[![PyPI version](https://badge.fury.io/py/numpy.svg)](https://badge.fury.io/py/numpy)
[![PyPI version](https://badge.fury.io/py/pandas.svg)](https://badge.fury.io/py/pandas)
[![PyPI version](https://badge.fury.io/py/matplot.svg)](https://badge.fury.io/py/matplot)

### DataParse is a tool that can help you in data anaylatics Basic Tasks

[CSV Model for trainnig](https://github.com/LoaiEsam37/csv)

[Installation](#Installation) | [Usage](#Usage) | [Functions](#Functions) | [Concat](#Concat) | [DropNa](#DropNa) | [DropColumn](#DropColumn) | [DropRow](#DropRow) | [DropDuplicates](#DropDuplicates) | [ConvertToDateTime](#ConvertToDateTime) | [ConvertToInt](#ConvertToInt) | [ExtractDate](#ExtractDate) | [MathMatics](#MathMatics) | [Statics](#Statics) | [Operations](#Operations) | [Linear](#Linear) | [Polynomial](#Polynomial) | [Display](#Display) | [Histogram](#Histogram) | [Bar](#Bar) | [Plot](#Plot) | [Scatter](#Scatter)

# Installation
    $ git clone https://github.com/LoaiEsam37/DataParse
    $ cd DataParse
    $ sudo chmod u+x setup.sh
    $ sudo chmod u+x main.py
    $ ./setup.sh
    $ ./main.py

if you have a problem with running **./main.py**
try to change the first line in **main.py** from **~~#!/bin/bash/python3~~**
to **#!/bin/bash/python3.10**
It depends on what version you have on your pc.

    $ cd
    $ nano .bashrc

* add this line ***alias dataparse='python3 Foo/bar/DataParse/main.py'*** 

* close the terminal and open it again

```
$ dataparse
```

# Usage

# Functions

## Concat

### This Function is for concat a directory that full of csv files into a single file

* Here we have a directory that i want to concat to ``all.csv``

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(1).png)

```
$ dataparse
```

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(2).png)

## DropNa

### This Function is for drop all NaN in csv file

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(3).png)

## DropColumn

### This Function is for drop the column from csv file that you want

* steps

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(4).png)

## DropRow

### This Function is for drop the row from csv file that you want

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(5).png)

## DropDuplicates

### This Function is for drop duplicates from the Column that you want

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(6).png)

## ConvertToDateTime

### This Function is to convert Column Values into DateTime

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(7).png)

## ConvertToInt

### This Function is to convert Column Values into Int

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(8).png)

## ExtractDate

### This Function is to Extract a Specific kind of date from another Column like: Year, Month, Day, Hour

* In This Example We have ``Order Date`` Column and We Want to Extract The Day from it and Put The Values to A new Column named ``Day``:

|    | Product                | Quantity Ordered   |   Price Each | Order Date          | Purchase Address                         |
|---:|:-----------------------|:-------------------|:-------------|:--------------------|:-----------------------------------------|
|  0 | LG Dryer               | 1                  |       600    | 2019-03-09 16:34:00 | 683 12th St, Los Angeles, CA 90001       |
|  1 | LG Washing Machine     | 1                  |       600    | 2019-09-18 17:32:00 | 925 Forest St, San Francisco, CA 94016   |
|  2 | Vareebadd Phone        | 1                  |       400    | 2019-06-09 14:02:00 | 853 5th St, Los Angeles, CA 90001        |              |
|  3 | 20in Monitor           | 1                  |       109.99 | 2019-09-18 09:10:00 | 188 11th St, Austin, TX 73301            |
|  4 | 27in FHD Monitor       | 1                  |       149.99 | 2019-09-14 16:06:00 | 172 Washington St, Los Angeles, CA 90001 |
|  5 | Flatscreen TV          | 1                  |       300    | 2019-09-18 14:54:00 | 930 North St, Seattle, WA 98101          |
|  6 | Macbook Pro Laptop     | 1                  |      1700    | 2019-09-29 13:37:00 | 926 North St, San Francisco, CA 94016    |
|  7 | Wired Headphones       | 1                  |        11.99 | 2019-09-18 10:13:00 | 877 Lincoln St, Boston, MA 02215         |
|  8 | 27in 4K Gaming Monitor | 1                  |       389.99 | 2019-09-24 22:16:00 | 501 Adams St, Seattle, WA 98101          |

* steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(9).png)

* Result :

|    | Product                | Quantity Ordered   |   Price Each | Order Date          | Purchase Address                         |   Day |
|---:|:-----------------------|:-------------------|:-------------|:--------------------|:-----------------------------------------|:------|
|  0 | LG Dryer               | 1                  |       600    | 2019-03-09 16:34:00 | 683 12th St, Los Angeles, CA 90001       |     9 |
|  1 | LG Washing Machine     | 1                  |       600    | 2019-09-18 17:32:00 | 925 Forest St, San Francisco, CA 94016   |    18 |
|  2 | Vareebadd Phone        | 1                  |       400    | 2019-06-09 14:02:00 | 853 5th St, Los Angeles, CA 90001        |     9 |                     |   nan |
|  3 | 20in Monitor           | 1                  |       109.99 | 2019-09-18 09:10:00 | 188 11th St, Austin, TX 73301            |    18 |
|  4 | 27in FHD Monitor       | 1                  |       149.99 | 2019-09-14 16:06:00 | 172 Washington St, Los Angeles, CA 90001 |    14 |
|  5 | Flatscreen TV          | 1                  |       300    | 2019-09-18 14:54:00 | 930 North St, Seattle, WA 98101          |    18 |
|  6 | Macbook Pro Laptop     | 1                  |      1700    | 2019-09-29 13:37:00 | 926 North St, San Francisco, CA 94016    |    29 |
|  7 | Wired Headphones       | 1                  |        11.99 | 2019-09-18 10:13:00 | 877 Lincoln St, Boston, MA 02215         |    18 |
|  8 | 27in 4K Gaming Monitor | 1                  |       389.99 | 2019-09-24 22:16:00 | 501 Adams St, Seattle, WA 98101          |    24 |

# MathMatics

## Statics

### This Function is to get the mean, mode, median, standard deviation, variance, min, max

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(10).png)

* Result :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(11).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(12).png)

## Operations

* This Function is to Sum, Subtract, Divide, Multiply Two Columns and put the value in a new Column

* In This Example we need to Multiply ``Quantity Ordered`` with ``Price Each`` and put the values in a new Column named ``Sales`` 

|    | Product                |   Quantity Ordered |   Price Each | Order Date          | Purchase Address                       |
|---:|:-----------------------|-------------------:|-------------:|:--------------------|:---------------------------------------|
|  0 | Product                |                nan |       nan    | nan                 | Purchase Address                       |
|  1 | AAA Batteries (4-pack) |                  3 |         2.99 | 2019-09-17 20:56:00 | 840 Highland St, Los Angeles, CA 90001 |
|  2 | USB-C Charging Cable   |                  1 |        11.95 | 2019-09-30 00:18:00 | 250 Meadow St, San Francisco, CA 94016 |
* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(13).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(14).png)

* Result :

|    | Product                |   Quantity Ordered |   Price Each | Order Date          | Purchase Address                       |   Sales |
|---:|:-----------------------|-------------------:|-------------:|:--------------------|:---------------------------------------|--------:|
|  0 | Product                |                nan |       nan    | nan                 | Purchase Address                       |  nan    |
|  1 | AAA Batteries (4-pack) |                  3 |         2.99 | 2019-09-17 20:56:00 | 840 Highland St, Los Angeles, CA 90001 |    8.97 |
|  2 | USB-C Charging Cable   |                  1 |        11.95 | 2019-09-30 00:18:00 | 250 Meadow St, San Francisco, CA 94016 |   11.95 |

## Linear

### This Function is to Do Linear Equation

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(17).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(18).png)

* [Next step](#Plot) to Show the Data on Matplotlib

## Polynomial

### This Function is to do Polynomial Equation

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(19).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(20).png)

* [Next step](#Plot) to Show the Data on Matplotlib

# Display

## Histogram

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(21).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(22).png)

* Result :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(23).png)

## Bar

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(24).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(25).png)

* Result :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(26).png)

## Plot

* CSV :

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(27).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(28).png)

* Result :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(29).png)

* JSON :

* [Linear](#Linear) :

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(31).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(32).png)

* Result :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(33).png)

* [Polynomial](#Polynomial) :

* Steps :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(34).png)

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(35).png)

* Result :

![](https://github.com/LoaiEsam37/Images/blob/main/dataparse(36).png)

## Scatter

## Connect Me

<a href="https://linkedin.com/in/loai-esam-109971215" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="loai-esam-109971215" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/loaiesam27" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="loaiesam27" height="30" width="40" /></a>
<a href="https://fb.com/loai.esam.16" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="loai.esam.16" height="30" width="40" /></a>
</p>


