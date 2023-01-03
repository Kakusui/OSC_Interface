import pyautogui as gui ## imports
import random as r 
import time
import keyboard as key
import mouse 
import os
import shutil
import sys
import threading
import filecmp
import logging
import subprocess
import threading
import smtplib
import ssl
import socket
import maskpass
import msvcrt
import mysql.connector

sys.path.insert(0, r'C:\Users\Tetra\Documents\GitHub\SAPH\\SMFVF') ## adds SMFVF.py to module import path

#SMFVF holds functions that are used across SAPH and its Dependencies, they are listed here for ease of access.

## exitR() is used to ensure proper auth disengage when SAPH is exited correctly
## ecset() also known as Element Comma Seperated Editor Tool is uses to edit txt files that store data like this "exitR,ecset,clearStream,userConfirm,inputCheck,"
## clearStream()  ensures that keys read by the keyboard module are not shown on the console when requesting regular keyboard input
## userConfirm() is used to ensure the user input was what they wanted to input, specifically used when writing to files where changing your mind is a hassle
## inputCheck() is used to ensure the userInput is valid, no matter the situation
## readLoopData() is used to access the Program wide modeNum,roundCount, and correctRounds,wantSound variables
## encrypt() is used to encrypt values
## decrypt() is used to decrypt values
## addToItypos is used to update itypos in the nusevei database
## addToTypos is used to update typos in the nusevei database
## createConnection is used to create a connection to the nusevei database
## executeQuery is used to send a query to the nusevei database where the result is not needed
## readQuery is used to send a query to the nusevei database where the result is needed

from time import sleep ## from imports
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from ctypes import *
from apiclient.http import MediaFileUpload
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from playsound import playsound
from datetime import datetime
from SMFVF_S import *

#-------------------Start-of-getFilePath()-------------------------------------------------

def getFilePath(Set): # since backup_s.py retrivels various files from the cloud, this decides where they go

    directory = datetime.today().strftime('%Y-%m-%d') # gets current date which is used for the directory name
    
    if(Set == 1):
        
        path = os.path.join(r"C:\Users\Tetra\Desktop\SCFS\NisoMehademaRakasuni",directory)
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\NisoMehademaRakasuni\Current Iteration\iteration.txt", "r+",encoding="utf8")
        Iteration = int(file1.read())
        file1.close()

        if(os.path.isdir(path) == False): # if directory for date does not exist please create then reset iterative count
           os.mkdir(path, 0o666)
           Iteration = 1
           
        dFile = path + "/" + directory + "-" + str(Iteration)
        Iteration += 1

        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\NisoMehademaRakasuni\Current Iteration\iteration.txt", "w+",encoding="utf8")
        file1.write(str(Iteration))
        file1.close()
        
    elif(Set == 2):
        
        path = os.path.join(r"C:\Users\Tetra\Desktop\SCFS\MehademaRakasuniKasunu",directory)
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\MehademaRakasuniKasunu\Current Iteration\iteration.txt", "r+",encoding="utf8")
        Iteration = int(file1.read())
        file1.close()

        if(os.path.isdir(path) == False): # if directory for date does not exist please create then reset iterative count
           os.mkdir(path, 0o666)
           Iteration = 1
           
        dFile = path + "/" + directory + "-" + str(Iteration)
        Iteration += 1

        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\MehademaRakasuniKasunu\Current Iteration\iteration.txt", "w+",encoding="utf8")
        file1.write(str(Iteration))
        file1.close()


    elif(Set == 3):
        
        path = os.path.join(r"C:\Users\Tetra\Desktop\SCFS\NuharunuNihamemekayahame",directory)
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\NuharunuNihamemekayahame\Current Iteration\iteration.txt", "r+",encoding="utf8")
        Iteration = int(file1.read())
        file1.close()

        if(os.path.isdir(path) == False): # if directory for date does not exist please create then reset iterative count
           os.mkdir(path, 0o666)
           Iteration = 1
           
        dFile = path + "/" + directory + "-" + str(Iteration)
        Iteration += 1
        
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\NuharunuNihamemekayahame\Current Iteration\iteration.txt", "w+",encoding="utf8")
        file1.write(str(Iteration))
        file1.close()

    elif(Set == 4):
        
        path = os.path.join(r"C:\Users\Tetra\Desktop\SCFS\rahahinukawa",directory)
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\rahahinukawa\Current Iteration\iteration.txt", "r+",encoding="utf8")
        Iteration = int(file1.read())
        file1.close()

        if(os.path.isdir(path) == False): # if directory for date does not exist please create then reset iterative count
           os.mkdir(path, 0o666)
           Iteration = 1
           
        dFile = path + "/" + directory + "-" + str(Iteration)
        Iteration += 1
        
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\rahahinukawa\Current Iteration\iteration.txt", "w+",encoding="utf8")
        file1.write(str(Iteration))
        file1.close()

    elif(Set == 5):
        
        path = os.path.join(r"C:\Users\Tetra\Desktop\SCFS\tafunuha",directory)
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\tafunuha\Current Iteration\iteration.txt", "r+",encoding="utf8")
        Iteration = int(file1.read())
        file1.close()

        if(os.path.isdir(path) == False): # if directory for date does not exist please create then reset iterative count
           os.mkdir(path, 0o666)
           Iteration = 1
           
        dFile = path + "/" + directory + "-" + str(Iteration)
        Iteration += 1
        
        file1 = open(r"C:\Users\Tetra\Desktop\SCFS\tafunuha\Current Iteration\iteration.txt", "w+",encoding="utf8")
        file1.write(str(Iteration))
        file1.close()

    return dFile # returns file path

#-------------------Start-of-main()-------------------------------------------------

os.system("title " + "Backup_S.py")

mfd_file_id,mfad_file_id,uploads,downloads,deletions = [],[],[],[],[]

i,progress,ii,aCount,limit = 0,0,0,0,7

aTrigger = False

exec(open(r"C:\Users\Tetra\Documents\GitHub\SAPH\SAU\SAU_S.py", errors='ignore').read())

print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Setting up Prerequisites for ABP)")

try:
  gauth = GoogleAuth()
  gauth.LocalWebserverAuth()
  drive = GoogleDrive(gauth)

except Exception as e:
  os.system('cls')
  print("Cloud Authentication Failed Due to : " + str(e))
  os.system('cls')
  exitR()

sleep(0.17)
gui.hotkey('ctrl', 'w')

sleep(0.17)

    
try: 
    gui.getWindowsWithTitle("Backup_S.py")[0].minimize()
except:
    pass
    
aCount+=1

os.system('cls')

print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Locating Folder\Path Addresses and Marking Appropriate Files for Deletion)")

SAPH_F = drive.ListFile({'q': "'1XhquHO4UE0MvhIzO1-hQ_bRr7bpQuaJT' in parents and trashed=false"}).GetList() # PythonStuff Level

SAPH_S_F = drive.ListFile({'q': "'17NZ3cLa3UfPrjIeQFYz3u-5WVcwzREAD' in parents and trashed=false"}).GetList() # SAPH Level

SAU_F = drive.ListFile({'q': "'1AVWBEg_tTvWEVmucCV6NCamInidAf8Hd' in parents and trashed=false"}).GetList() # SAU Level

SEDH_F = drive.ListFile({'q': "'1kZk5rEXJb5uzqT53gqR26SmkKrMwsjm9' in parents and trashed=false"}).GetList() # SEDH Level

SMFVF_F = drive.ListFile({'q': "'1O7lBBI6xzLEPm48CbYrP-IrUdduB9nuV' in parents and trashed=false"}).GetList() # SMFVF Level

NMR = drive.ListFile({'q': "'1I3Ka6B248m4iIXKAAUNleMRaabkUbuit' in parents and trashed=false"}).GetList() # NisoMehademaRakasuni Level
MRK = drive.ListFile({'q': "'1MkyGE-_w0oC0htysnSikom7djVLlQNH6' in parents and trashed=false"}).GetList() # MehademaRakasuniKasunu
NN = drive.ListFile({'q': "'1umKZCiLh5BG83oB8d7NZ6jJg0zD6L_J3' in parents and trashed=false"}).GetList() # NuharunuNihamemekayahame Level
R = drive.ListFile({'q': "'1KjfiXX6r9UGi7UX5VYb5SMJtSEwkjiS2' in parents and trashed=false"}).GetList() # Rahahinukawa Level
T = drive.ListFile({'q': "'1dfMMfbw4vkQI1YUCvBdhuvHbvMch44fn' in parents and trashed=false"}).GetList() # Tafunuha Level

SAPH_P = r"C:\Users\Tetra\Documents\GitHub\SAPH"

SAPH_S_P = r"C:\Users\Tetra\Documents\GitHub\SAPH\SAPH"

SAU_P = r"C:\Users\Tetra\Documents\GitHub\SAPH\SAU"

SEDH_P = r"C:\Users\Tetra\Documents\GitHub\SAPH\SEDH"

SMFVF_P = r"C:\Users\Tetra\Documents\GitHub\SAPH\SMFVF"

with open(r"C:\Users\Tetra\Documents\GitHub\SAPH\eL.txt", "r+",encoding="utf8") as ArrayRaw:
    excludeList = [x.strip() for x in ArrayRaw]

with open(r"C:\Users\Tetra\Documents\GitHub\SAPH\iL.txt", "r+",encoding="utf8") as ArrayRaw:
    includeList = [x.strip() for x in ArrayRaw]

for f in SAPH_F:
  if((f['title']) not in excludeList):
       mfd_file_id.append(f['id'])
       print("Marked " + str(f['title']))
        
for f in SAPH_S_F:
  if((f['title']) not in excludeList):
       mfd_file_id.append(f['id'])
       print("Marked " + str(f['title']))

for f in SAU_F:
  if((f['title']) not in excludeList):
       mfd_file_id.append(f['id'])
       print("Marked " + str(f['title']))

for f in SEDH_F:
  if((f['title']) not in excludeList):
       mfd_file_id.append(f['id'])
       print("Marked " + str(f['title']))

for f in SMFVF_F:
  if((f['title']) not in excludeList):
       mfd_file_id.append(f['id'])
       print("Marked " + str(f['title']))

aCount+=1
sleep(3)

while(i < len(mfd_file_id)):
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Deleting Old Files)")
    print("Querying " + str(i+1) + " of " + str(len(mfd_file_id)))
    f = drive.CreateFile({'id':  mfd_file_id[i]})
    deletions.append((f['title'])  + "\n")
    print("Trashing " + str(f['title']))
    f.Trash()
    print("Deleting " + str(f['title']))
    f.Delete()  
    i+=1
    os.system('cls')
    
i = 0

mfd_file_id.clear()

aCount+=1
    
for x in os.listdir(SAPH_P):
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Uploading SAPH)")
    print("Querying " + str(i+1) + " of " + str(len(os.listdir(SAPH_P))))
    i+=1
    if(os.path.isfile(x) == True or x in includeList and x not in excludeList):
        f = drive.CreateFile({'parents': [{'id': '1XhquHO4UE0MvhIzO1-hQ_bRr7bpQuaJT'}]})
        f.SetContentFile(os.path.join(SAPH_P, x))
        f['title'] = x
        print("Uploading " + str(x))
        f.Upload()
        f = None

i = 0
aCount+=1

for x in os.listdir(SAPH_S_P):
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Uploading SAPH_S and Its Dependencies)")
    print("Querying " + str(i+1) + " of " + str(len(os.listdir(SAPH_S_P))))
    i+=1
    if(os.path.isfile(x) == True or x in includeList and x not in excludeList):
        f = drive.CreateFile({'parents': [{'id': '17NZ3cLa3UfPrjIeQFYz3u-5WVcwzREAD'}]})
        f.SetContentFile(os.path.join(SAPH_S_P, x))
        f['title'] = x
        print("Uploading " + str(x))
        f.Upload()
        f = None

i = 0
aCount+=1

for x in os.listdir(SAU_P):
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Uploading SAU and Its Dependencies)")
    print("Querying " + str(i+1) + " of " + str(len(os.listdir(SAU_P))))
    i+=1
    if(os.path.isfile(x) == True or x in includeList and x not in excludeList):
        f = drive.CreateFile({'parents': [{'id': '1AVWBEg_tTvWEVmucCV6NCamInidAf8Hd'}]})
        f.SetContentFile(os.path.join(SAU_P, x))
        f['title'] = x
        print("Uploading " + str(x))
        f.Upload()
        f = None

i = 0
aCount+=1

for x in os.listdir(SEDH_P):
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Uploading SEDH and Its Dependencies)")
    print("Querying " + str(i+1) + " of " + str(len(os.listdir(SEDH_P))))
    i+=1
    if(os.path.isfile(x) == True or x in includeList and x not in excludeList):
        f = drive.CreateFile({'parents': [{'id': '1kZk5rEXJb5uzqT53gqR26SmkKrMwsjm9'}]})
        f.SetContentFile(os.path.join(SEDH_P, x))
        f['title'] = x
        print("Uploading " + str(x))
        f.Upload()
        f = None

i = 0
aCount+=1

for x in os.listdir(SMFVF_P):
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Uploading SMFVF and Its Dependencies)")
    print("Querying " + str(i+1) + " of " + str(len(os.listdir(SMFVF_P))))
    i+=1
    if(os.path.isfile(x) == True or x in includeList and x not in excludeList):
        f = drive.CreateFile({'parents': [{'id': '1O7lBBI6xzLEPm48CbYrP-IrUdduB9nuV'}]})
        f.SetContentFile(os.path.join(SMFVF_P, x))
        f['title'] = x
        print("Uploading " + str(x))
        f.Upload()
        f = None


i = 0
ii = 0
mfd_file_id.clear()
aTrigger = False

for f in NMR:
    if(aTrigger == False):
        limit+=1
        aCount+=1
    aTrigger = True
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Retrieving Valid NisoMehademaRakasuni(s)")
    print("Querying " + str(ii+1) + " of " + str(len(NMR)))
    ii+=1
    if((f['title']) not in excludeList):
        mfd_file_id.append(f['id'])
        mfad_file_id.append(f['id'])
        ff = drive.CreateFile({'id': mfd_file_id[i]})
        dFile = getFilePath(1)
        print("Downloading " + f['title'] + " as " + str(dFile))
        ff.GetContentFile(dFile + ".png")
        i+=1
        dFile = ""
        f = None
        ff = None
        
    os.system('cls')

i = 0
ii = 0
mfd_file_id.clear()
aTrigger = False

for f in MRK:
    if(aTrigger == False):
        limit+=1
        aCount+=1
    aTrigger = True
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Retrieving Valid MehademaRakasuniKasunu(s)")
    print("Querying " + str(ii+1) + " of " + str(len(MRK)))
    ii+=1
    if((f['title']) not in excludeList):
        mfd_file_id.append(f['id'])
        mfad_file_id.append(f['id'])
        ff = drive.CreateFile({'id': mfd_file_id[i]})
        dFile = getFilePath(2)
        print("Downloading " + f['title'] + " as " + str(dFile))
        ff.GetContentFile(dFile + ".png")
        i+=1
        dFile = "" 
        f = None
        ff = None
        
    os.system('cls')

i = 0
ii = 0
mfd_file_id.clear()
aTrigger = False

for f in NN:
    if(aTrigger == False):
        limit+=1
        aCount+=1
    aTrigger = True
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Retrieving Valid NuharunuNihamemekayahame(s)")
    print("Querying " + str(ii+1) + " of " + str(len(NN)))
    ii+=1
    if((f['title']) not in excludeList):
        mfd_file_id.append(f['id'])
        mfad_file_id.append(f['id'])
        ff = drive.CreateFile({'id': mfd_file_id[i]})
        dFile = getFilePath(3)
        print("Downloading " + f['title'] + " as " + str(dFile))
        ff.GetContentFile(dFile + ".png")
        dFile = ""
        i+=1
        dFile = ""
        f = None
        ff = None
        
    os.system('cls')

i = 0
ii = 0
mfd_file_id.clear()
aTrigger = False

for f in R:
    if(aTrigger == False):
        limit+=1
        aCount+=1
    aTrigger = True
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Retrieving Valid rahahinukawa(s)")
    print("Querying " + str(ii+1) + " of " + str(len(R)))
    ii+=1
    if((f['title']) not in excludeList):
        mfd_file_id.append(f['id'])
        mfad_file_id.append(f['id'])
        ff = drive.CreateFile({'id': mfd_file_id[i]})
        dFile = getFilePath(4)
        print("Downloading " + f['title'] + " as " + str(dFile))
        ff.GetContentFile(dFile + ".png")
        i+=1
        dFile = ""
        f = None
        ff = None
        
    os.system('cls')

i = 0
ii = 0
mfd_file_id.clear()
aTrigger = False

for f in T:
    if(aTrigger == False):
        limit+=1
        aCount+=1
    aTrigger = True
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + "  Processes - (Retrieving Valid tafunuha(s)")
    print("Querying " + str(ii+1) + " of " + str(len(T)))
    ii+=1
    if((f['title']) not in excludeList):
        mfd_file_id.append(f['id'])
        mfad_file_id.append(f['id'])
        ff = drive.CreateFile({'id': mfd_file_id[i]})
        dFile = getFilePath(5)
        print("Downloading " + f['title'] + " as " + str(dFile))
        ff.GetContentFile(dFile + ".png")
        i+=1
        dFile = ""
        f = None
        ff = None
        
    os.system('cls')

i = 0
ii = 0
mfd_file_id.clear()
aTrigger = False

while(i < len(mfad_file_id)):
    if(aTrigger == False):
        limit+=1
        aCount+=1
    aTrigger = True
    os.system('cls')
    print("Attempting ABP : " + str(aCount) + " of " + str(limit) + " Processes - (Removing Downloaded File(s) from Drive)")
    print("Querying " + str(i+1) + " of " + str(len(mfad_file_id)))
    f = drive.CreateFile({'id':  mfad_file_id[i]})
    print("Trashing " + str(f['title']))
    f.Trash()
    print("Deleting " + str(f['title']))
    f.Delete()  
    i+=1
    f = None

os.system('cls')
