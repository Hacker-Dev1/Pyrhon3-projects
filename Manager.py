'''
File: FILENAME: Manager
Author: Jack Burkett III  (15 y/o, 5 m/o)
Description: GUI and Information retreiver
'''
import pydirectinput
import os
import time
import pyinstaller

try:
    import thread
except:
    print("there is no threading module")
    print("well, i can't do anything about it, so contact the developer")
    time.sleep(3)

#*******************************************************************************
#Better Description
"""
This is the Manager program. it manages the threads that compile multiple
things at one time, or deals with information that makes the compilers do thier
job and do it quickly.
"""
def C():
    os.system('cygnus.exe')
    time.sleep(5)
    pydirectinput.write('cd "') + Path1 + ('"')
    time.sleep(0.5)
    pydirectinput.press("enter")
    time.sleep(2)
    pydirectinput.write('g++ "') + File1 + ('" "') + File1[-3:] + ('".exe')
    pydirectinput.press("enter")

def Cpp():
    os.system('cygnus.exe')
    time.sleep(5)
    pydirectinput.write('cd "') + Path1 + ('"')
    time.sleep(0.5)
    pydirectinput.press("enter")
    time.sleep(2)
    pydirectinput.write('g++ "') + File1 + ('" "') + File1[-3:] + ('".exe')
    pydirectinput.press("enter")

"""
def Java():
    os.system('start Java_to_C++_Converter.exe')
    time.sleep(5)
    pydirectinput.click(446,878)
    time.sleep(0.25)
    pydirectinpt.click(373,797)
    time.sleep(0.25)
    pydirectinput.write(File1)
    time.sleep(0.025)
    pydirectinput.press("enter")
    pydirectinput.click(981,875)
    time.sleep(0.5)
    pydirectinput.write(File1[-3:])
    pydirectinput.press("enter")
    print("Next part")
    File1 = File1 + str('.cpp')
    JavaCPPProcessor.Process()

def Typescript():

"""
def Python():
    os.system('start powershell.exe')
    time.sleep(5)
    pydirectinput.write('pyinstaller --onefile "') + File1 + ('"')
    pydirectinput.press("enter")

#*******************************************************************************
#actual thread starts
def OneThread(Thread1):
    if Type1 == 'C':
        C()
    elif Type1 == 'C++':
        Cpp()
    #elif Type1 == 'Java':
    #    Java()
    elif Type1 == 'Python':
        Python()
    #elif Type1 == 'Typescript':
    #   Typescript()

def TwoThread(Thread2):
    if Type2 == 'C':
        Ctwo()
    elif Type2 == 'C++':
        Cpptwo()
    #elif Type2 == 'Java':
        #Javatwo()
    elif Type2 == 'Python':
        Pythontwo()
    #elif Type2 == 'Typecript':
        #Typecripttwo()

def ThreeThread(Thread3):
    if Type3 == 'C':
        Cthree()
    elif Type3 == 'C++':
        Cppthree()
    #elif Type3 == 'Java':
        #Javathree()
    elif Type3 == 'Python':
        Pythonthree()
    #elif Type3 == 'Typecript':
        #Typecriptthree()

def FourThread(Thread4):
    if Type4 == 'C':
        Cfour()
    elif Type4 == 'C++':
        Cppfour()
    #elif Type4 == 'Java':
        #Javafour()
    elif Type4 == 'Python':
        Pythonfour()
    #elif Type4 == 'Typecript':
        #Typecriptfour()
#*******************************************************************************
#Functions of Functions
def onONE():
    try:
        thread.start_new_thread( OneThread, ("Thread-1", 2 ) )
    except:
        print("failed to compile. thread failed to start")

def TwoThreads():
    try:
        thread.start_new_thread( OneThread, ("Thread-1", 2 ) )
        thread.start_new_thread( TwoThread, ("Thread-2", 4 ) )
    except:
        print("failed to compile. threads failed to start")

def ThreeThreads():
    try:
        thread.start_new_thread( OneThread, ("Thread-1", 2 ) )
        thread.start_new_thread( TwoThread, ("Thread-2", 4 ) )
        thread.start_new_thread( ThreeThread, ("Thread-3", 6) )
    except:
        print("failed to compile. threads failed to start")

def FourThreads():
    try:
        thread.start_new_thread( OneThread, ("Thread-1", 2 ) )
        thread.start_new_thread( TwoThread, ("Thread-2", 4 ) )
        thread.start_new_thread( ThreeThread, ("Thread-3", 6) )
        thread.start_new_thread( FourThread, ("Thread-4", 8) )
    except:
        print("failed to compile. threads failed to start")

#*******************************************************************************
#Manager of how many threads actually start

def ThreadActive():
    if ThreadNum == 1:
        onONE()
    elif ThreadNum == 2:
        TwoThreads()
    elif ThreadNum == 3:
        ThreeThreads()
    elif ThreadNum == 4:
        FourThreads()
