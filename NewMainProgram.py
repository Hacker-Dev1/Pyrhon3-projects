"""
FileName: MainProgram
Author: Jack Burkett III (15y/o, 5 or 6 m/o (its the end of the month.))
Description: IDE-free GUI based compiler
"""
import os
os.system('start loadingbar.exe')
import time
import tkinter as tk
#import Manager
time.sleep(2.5)
os.system('TASKKILL /im loadingbar.exe')

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

print("welcome to the terminal. you won't be here long. you have up to 4 threads to")
print("compile with. this is how many files you can can turn into executables")
ThreadNum = input()
if ThreadNum == 4:
    print("This version of the program only supports 4 threads.")
    print("If you want more threads available then get the Professional version")
    time.sleep(5)
    os.system('start MainProgram.exe')
    exit()

"""
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

width=75, foreground="white",
height=20,background="#012456",


"""

#****************************************************************************************
#Main Program into frames

IDEfreeGUI = tk.Tk()

frame_1 = tk.Frame()
label = tk.Label(master=frame_1, fg="white", bg="#012456", width=75, height=20)
label.pack()

frame_2 = tk.Frame()
label2 = tk.Label(master=frame_2,
    text="IDE-less 8 thread Compiler {1.0.43}",
    fg="white", bg="#012456")
label2.place(x=0, y=0)

frame_3 = tk.Frame()
label3 = tk.Label(master=frame_3,
    text="for C, C++, Java, Python 3, Typescript",
    fg="white", bg="#012456"
    )
label3.place(x=0, y=20)

frame_4 = tk.Frame()
label4 = tk.Label(master=frame_4,
    text="-------------------------------------",
    fg="#CC0000", bg="#012456"
    )
label4.place(x=0, y=40)

frame_5 = tk.Frame()
label5 = tk.Label(master=frame_5,
    text="State the file name without the extension:",
    fg="white", bg="#012456"
    )
label.place(x=0, y=60)

frame_6 = tk.Frame()
entry1 = tk.Entry(master=frame_6)
entry1.place(x=250, y=60)

frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
frame_6.pack()

IDEfreeGUI.mainloop()
