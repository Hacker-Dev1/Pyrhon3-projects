'''
File: FILENAME:BackupProgram
Author: Jack Burkett III  (15 y/o, 5 m/o)
Description: Terminal and Information retreiver
'''

import os
import time
os.system('start loadingbar.exe')
time.sleep(6)
os.system('TASKKILL /im loadingbar.exe')

try:
    import Manager
except:
    print("ERROR : ABSOLUTELY required file <Manager.dll> is missing")
"""
    print("exiting in: 5 seconds")
    os.system("start loadingbar.exe")
    time.sleep(5)
    os.system('TASKKILL /im loadingbar.exe')
    exit()
"""
#****************************************************************************************
#deeper description
"""
This Program will use other compilers. they may or may not be the one you like to use
    but for every compiler I use, it may have been the only compiler that works for free
    This program is free, but it can only run four files at a time. the Professional
        edition can compile 32 files at once and is also more efficient.
        it is suggested that you make your own
        program to manage the files because my guess is that you may be using a server
    The Professional GUI compiler is $300 for 2 years.
File types that are compiled>>>

C

C++ (file extension should be '.cpp')

Java (I found a converter to C++ and i use three steps to compile these)
    Java free converter is only usable up to 100 lines.

Python 3.7/3.8/3.9

Typescript (which compiles to Javascript. Typescript is just a better version of Javascript)
"""
#*******************************************************************************
#Values used

ThreadNum = input("How many threads do you want to use, better be at most four, or else this program will reject it and restart")
if ThreadNum >= '4':
    print("This version of the program only supports 4 threads.")
    time.sleep(5)
    try:
        os.system('start MainProgram.py')
    except:
        os.system('start MainProgram.exe')

print(" ")
print("As you may notice, this program is smaller, lighter, and was easier to program.")
print("this is because GUIs are complex and difficult to work with. if we are using a")
print("terminal, then all data values are directly applied to their vaiables. making this ")
print("program run significantly faster at the salty cost of no promised GUI")
print(">>>")
print("WELL. lets get to work. im going to question you with 12 different variables")
print("if you dont have any information for anymore files, JUST PRESS ENTER")

File1 = input("File names first: give first file's name:")
File2 = input("second File's name:")
File3 = input("third File's name:")
File4 = input("fourth files name. this would be the last thread this program can use:")

Type1 = input("File types next >> first file's type:")
Type2 = input("second File's type:")
Type3 = input("third Files's type:")
Type4 = input("fourth File's type:")

Path1 = input("Last yet not least, File Paths:")
Path2 = input("second file's path:")
Path3 = input("third File's path:")
Path4 = input("fouth and last peice of data, Path:")

def Manage():
    if ThreadNum == 1:
        Manager.ThreadActive()
    elif ThreadNum == 2:
        Manager.ThreadActive()
    elif ThreadNum == 3:
        Manager.ThreadActive()
    elif ThreadNum == 4:
        Manager.ThreadActive()

Manage()
