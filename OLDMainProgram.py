"""
File: FILENAME:MainProgram
Author: Jack Burkett III  (15 y/o, 5 m/o)
Description: GUI and Information retriever
"""

import os
import time

os.system('start loadingbar.exe')
time.sleep(6)
os.system('TASKKILL /im loadingbar.exe')

import pysimplegui as sg
import Manager

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
#***************************************************************************************
#Values used

ThreadNum = input("this may be a terminal, but just type how many threads you need")
if ThreadNum >= 4:
    print("This version of the program only supports 4 threads.")
    print("If you want more threads available then get the Professional version")
    time.sleep(5)
    os.system('start MainProgram.exe')

File1 == 0
File2 == 0
File3 == 0
File4 == 0

Type1 == ''
Type2 == ''
Type3 == ''
Type4 == ''

Path1 == ''
Path2 == ''
Path3 == ''
Path4 == ''

#**********************************
# For repairs or upgrades

"""
sg.theme('Dark Blue 3')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
"""

#****************************************************************************************
#NOW with the GUI
#got layout from (https://pysimplegui.readthedocs.io/en/latest/)

if ThreadNum == 1:
    sg.theme('Dark Blue 3')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('OK, Welcome to inputing file info into a GUI!')],
                [sg.Text('Input your file name'), sg.InputTextFileone()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypeone()],
                [sg.Text('Input your file path'), sg.InputTextPathone()],
                [sg.Button('Compile'), sg.Button('Cancel')] ]

if ThreadNum == 2:
    sg.theme('Dark Blue 3')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('OK, Welcome to inputing file info into a GUI!')],
                [sg.Text('Input your file name'), sg.InputTextFileone()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypeone()],
                [sg.Text('Input your file path'), sg.InputTextPathone()],
                #File info 2
                [sg.Text('Input your file name'), sg.InputTextFiletwo()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypetwo()],
                [sg.Text('Input your file path'), sg.InputTextPathtwo()],
                [sg.Button('Compile'), sg.Button('Cancel')] ]

if ThreadNum == 3:
    sg.theme('Dark Blue 3')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('OK, Welcome to inputing file info into a GUI!')],
                [sg.Text('Input your file name'), sg.InputTextFileone()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypeone()],
                [sg.Text('Input your file path'), sg.InputTextPathone()],
                #File info 2
                [sg.Text('Input your file name'), sg.InputTextFiletwo()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypetwo()],
                [sg.Text('Input your file path'), sg.InputTextPathtwo()],
                #File info 3
                [sg.Text('Input your file name'), sg.InputTextFilethree()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypethree()],
                [sg.Text('Input your file path'), sg.InputTextPaththree()],
                [sg.Button('Compile'), sg.Button('Cancel')] ]

if ThreadNum == 4:
    sg.theme('Dark Blue 3')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('OK, Welcome to inputing file info into a GUI!')],
                [sg.Text('Input your file name'), sg.InputTextFileone()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypeone()],
                [sg.Text('Input your file path'), sg.InputTextPathone()],
                #File info 2
                [sg.Text('Input your file name'), sg.InputTextFiletwo()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypetwo()],
                [sg.Text('Input your file path'), sg.InputTextPathtwo()],
                #File info 3
                [sg.Text('Input your file name'), sg.InputTextFilethree()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypethree()],
                [sg.Text('Input your file path'), sg.InputTextPaththree()],
                #File info 4
                [sg.Text('Input your file name'), sg.InputTextFilefour()],
                [sg.Text('File Type? C / C++ / Java / Python / Typescript ?')],
                [sg.InputTypefour()],
                [sg.Text('Input your file path'), sg.InputTextPathfour()],
                [sg.Button('Compile'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Compiler+GUI 0.3.1', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Compile':
        break
        try:
            manage()
            print("Compiling")
        except:
            print("ERROR:")
            print("{")
            print("There was probably a problem operating one of the")
            print("required compilers or the information was invalid")
            print("FOR ERROR INFORMATION: go to compiler window to see its error")
            print("}")
    #no matter how many threads, the values will equal its value
    #not to mention that the Manager will only start as many threads as needed
    #Files
    sg.InputTextFileone == File1
    sg.InputTextFiletwo == File2
    sg.InputTextFilethree == File3
    sg.InputTextFilefour == File4
    #File Types
    sg.InputTypeone == Type1
    sg.InputTypetwo == Type2
    sg.InputTypethree == Type3
    sg.InputTypefour == Type4
    #File Paths
    sg.InputTextPathone == Path1
    sg.InputTextPathtwo == Path2
    sg.InputTextPaththree == Path3
    sg.InputTextPathfour == Path4
    #Compiler Manager Time (FINALLY)

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

time.sleep(360)
exit()