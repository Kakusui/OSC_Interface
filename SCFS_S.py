import pyautogui as gui ## imports
import os
import shutil

from time import sleep ## from imports
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from ctypes import *
from apiclient import discovery
from datetime import datetime

#-------------------Start-of-startup()-------------------------------------------------

def startup():
    
    scf1 = r'C:\Users\Tetra\Desktop\SCF'

    tafunuha = r'C:\Users\Tetra\Desktop\SCF\tafunuha'
    rahahinukawa = r'C:\Users\Tetra\Desktop\SCF\rahahinukawa'
    NuharunuNihamemekayahame = r'C:\Users\Tetra\Desktop\SCF\NuharunuNihamemekayahame'
    NisoMehademaRakasuni = r'C:\Users\Tetra\Desktop\SCF\NisoMehademaRakasuni'
    MehademaRakasuniKasunu = r'C:\Users\Tetra\Desktop\SCF\MehademaRakasuniKasunu'

    tafunuha2 = r'C:\Users\Tetra\Desktop\SCF\tafunuha\Current Iteration'
    rahahinukawa2 = r'C:\Users\Tetra\Desktop\SCF\rahahinukawa\Current Iteration'
    NuharunuNihamemekayahame2 = r'C:\Users\Tetra\Desktop\SCF\NuharunuNihamemekayahame\Current Iteration'
    NisoMehademaRakasuni2 = r'C:\Users\Tetra\Desktop\SCF\NisoMehademaRakasuni\Current Iteration'
    MehademaRakasuniKasunu2 = r'C:\Users\Tetra\Desktop\SCF\MehademaRakasuniKasunu\Current Iteration'

    tafunuha3 = r'C:\Users\Tetra\Desktop\SCF\tafunuha\Current Iteration\iteration.txt'
    rahahinukawa3 = r'C:\Users\Tetra\Desktop\SCF\rahahinukawa\Current Iteration\iteration.txt'
    NuharunuNihamemekayahame3 = r'C:\Users\Tetra\Desktop\SCF\NuharunuNihamemekayahame\Current Iteration\iteration.txt'
    NisoMehademaRakasuni3 = r'C:\Users\Tetra\Desktop\SCF\NisoMehademaRakasuni\Current Iteration\iteration.txt'
    MehademaRakasuniKasunu3 = r'C:\Users\Tetra\Desktop\SCF\MehademaRakasuniKasunu\Current Iteration\iteration.txt'

    if(os.path.isdir(scf1) == False):
        os.mkdir(scf1, 0o666)
        print(scf1 + " created due to lack of the folder")
        sleep(.1)


    if(os.path.isdir(tafunuha) == False):
        os.mkdir(tafunuha, 0o666)
        print(tafunuha + " created due to lack of the folder")
        sleep(.1)


    if(os.path.isdir(rahahinukawa) == False):
        os.mkdir(rahahinukawa, 0o666)
        print(rahahinukawa + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(NuharunuNihamemekayahame) == False):
        os.mkdir(NuharunuNihamemekayahame, 0o666)
        print(NuharunuNihamemekayahame + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(NisoMehademaRakasuni) == False):
        os.mkdir(NisoMehademaRakasuni, 0o666)
        print(NisoMehademaRakasuni + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(MehademaRakasuniKasunu) == False):
        os.mkdir(MehademaRakasuniKasunu, 0o666)
        print(MehademaRakasuniKasunu + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(tafunuha2) == False):
        os.mkdir(tafunuha2, 0o666)
        print(tafunuha2 + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(rahahinukawa2) == False):
        os.mkdir(rahahinukawa2, 0o666)
        print(rahahinukawa2 + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(NuharunuNihamemekayahame2) == False):
        os.mkdir(NuharunuNihamemekayahame2, 0o666)
        print(NuharunuNihamemekayahame2 + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(NisoMehademaRakasuni2) == False):
        os.mkdir(NisoMehademaRakasuni2, 0o666)
        print(NisoMehademaRakasuni2 + " created due to lack of the folder")
        sleep(.1)

    if(os.path.isdir(MehademaRakasuniKasunu2) == False):
        os.mkdir(MehademaRakasuniKasunu2, 0o666)
        print(MehademaRakasuniKasunu2 + " created due to lack of the folder")
        sleep(.1)

    if(os.path.exists(tafunuha3) == False):
        print(tafunuha3 + " was created due to lack of the file")
        with open(tafunuha3, "w+", encoding="utf-8") as file:
            file.write("0")

    if(os.path.exists(rahahinukawa3) == False):
        print(rahahinukawa3 + " was created due to lack of the file")
        with open(rahahinukawa3, "w+", encoding="utf-8") as file:
            file.write("0")

    if(os.path.exists(NuharunuNihamemekayahame3) == False):
        print(NuharunuNihamemekayahame3 + " was created due to lack of the file")
        with open(NuharunuNihamemekayahame3, "w+", encoding="utf-8") as file:
            file.write("0")

    if(os.path.exists(NisoMehademaRakasuni3) == False):
        print(NisoMehademaRakasuni3 + " was created due to lack of the file")
        with open(NisoMehademaRakasuni3, "w+", encoding="utf-8") as file:
            file.write("0")

    if(os.path.exists(MehademaRakasuniKasunu3) == False):
        print(MehademaRakasuniKasunu3 + " was created due to lack of the file")
        with open(MehademaRakasuniKasunu3, "w+", encoding="utf-8") as file:
            file.write("0")
        

#-------------------Start-of-download_files()-------------------------------------------------

def download_files(gfolder_id, mfad_file_id,Set):
    
    i = 0
    
    query = "mimeType != 'application/vnd.google-apps.folder' and trashed = false and '{}' in parents".format(gfolder_id)
    fileList = drive.ListFile({'q': query}).GetList()

    for f in fileList:
        mfad_file_id.append(f['id'])
        ff = drive.CreateFile({'id': f['id']})
        dFile = get_file_path(Set)
        print("Downloading {} as {}".format(f['title'], dFile))
        ff.GetContentFile(dFile + ".png")
        i += 1
        dFile = ""
        f = None
        ff = None

    return mfad_file_id

#-------------------Start-of-mark_files()-------------------------------------------------

def mark_files(gfolder,mfd_file_id): ## used to mark files for deletion
    
    for f in gfolder:
        mfd_file_id.append(f['id'])
        print("Marked " + str(f['title']))

    return mfd_file_id

#-------------------Start-of-delete_files()-------------------------------------------------

def delete_files(mfd_file_id):

    i = 0
    service = discovery.build('drive', 'v3', credentials=gauth.credentials)
    batch = service.new_batch_http_request(callback=None)

    while i < len(mfd_file_id):
        f = drive.CreateFile({'id':  mfd_file_id[i]})
        print("Trashing {}".format(f['title']))
        batch.add(service.files().delete(fileId=f['id']))
        i += 1

    batch.execute()
    print("Deleting files")

#-------------------Start-of-get_file_path()-------------------------------------------------

def get_file_path(Set): ## used to determine where files downloaded from the drive will go
    
    directory = datetime.today().strftime('%Y-%m-%d')

    filePaths = {
        1: r"C:\Users\Tetra\Desktop\SCF\NisoMehademaRakasuni",
        2: r"C:\Users\Tetra\Desktop\SCF\MehademaRakasuniKasunu",
        3: r"C:\Users\Tetra\Desktop\SCF\NuharunuNihamemekayahame",
        4: r"C:\Users\Tetra\Desktop\SCF\rahahinukawa",
        5: r"C:\Users\Tetra\Desktop\SCF\tafunuha",
    }
    iterationPaths = {
        1: r"C:\Users\Tetra\Desktop\SCF\NisoMehademaRakasuni\Current Iteration\iteration.txt",
        2: r"C:\Users\Tetra\Desktop\SCF\MehademaRakasuniKasunu\Current Iteration\iteration.txt",
        3: r"C:\Users\Tetra\Desktop\SCF\NuharunuNihamemekayahame\Current Iteration\iteration.txt",
        4: r"C:\Users\Tetra\Desktop\SCF\rahahinukawa\Current Iteration\iteration.txt",
        5: r"C:\Users\Tetra\Desktop\SCF\tafunuha\Current Iteration\iteration.txt",
    }
    
    path = os.path.join(filePaths[Set], directory)

    with open(iterationPaths[Set], "r", encoding="utf8") as f:
        Iteration = int(f.read())

    os.makedirs(path, exist_ok=True)
    dFile = path + "/" + directory + "-" + str(Iteration)
    Iteration += 1

    with open(iterationPaths[Set], "w", encoding="utf8") as f:
        f.write(str(Iteration))

    return dFile

#-------------------Start-of-move_scf()-------------------------------------------------

def move_scf():
    
    drivePath = "E:\\" # Replace this with the path of the drive you want to check

    if os.path.exists(drivePath):
        pass
    else:
        return

    scf1 = r'C:\Users\Tetra\Desktop\SCF'
    scf2 = r'E:\SCF'

    if os.path.isdir(scf2) == False:
        os.mkdir(scf2, 0o666)
        print(scf2 + " created due to lack of the folder")

    for subDir, files in os.walk(scf1):

        destinationSubDir = subDir.replace(scf1, scf2, 1)
        os.makedirs(destinationSubDir, exist_ok=True)

        for file in files:

            sourcePath = os.path.join(subDir, file)
            destinationPath = os.path.join(destinationSubDir, file)
            shutil.copy(sourcePath, destinationPath)

    shutil.rmtree(scf1)

#-------------------Start-of-main()-------------------------------------------------

os.system("title " + "SCFS_S.py")

startup()

sleep(.17)

try: 
    gui.getWindowsWithTitle("SCFS_S.py")[0].minimize()
except:
    pass

mfd_file_id,mfad_file_id = [],[]

try:
    clientJsonPath = "C:\\ProgramData\\SCFS\\client_secrets.json"
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = clientJsonPath
    
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

except Exception as e:
  os.system('cls')
  print("Cloud Authentication Failed Due to : " + str(e))
  os.system('pause')
  exit()

sleep(0.17)
gui.hotkey('ctrl', 'w')

mfad_file_id = download_files('1I3Ka6B248m4iIXKAAUNleMRaabkUbuit',mfad_file_id,1) ## NisoMehademaRakasuni Level

mfad_file_id = download_files('1MkyGE-_w0oC0htysnSikom7djVLlQNH6',mfad_file_id,2) ## MehademaRakasuniKasunu

mfad_file_id = download_files('1umKZCiLh5BG83oB8d7NZ6jJg0zD6L_J3',mfad_file_id,3) ## NuharunuNihamemekayahame Level

mfad_file_id = download_files('1KjfiXX6r9UGi7UX5VYb5SMJtSEwkjiS2',mfad_file_id,4) ## Rahahinukawa Level

mfad_file_id = download_files('1dfMMfbw4vkQI1YUCvBdhuvHbvMch44fn',mfad_file_id,5) ## Tafunuha Level

delete_files(mfad_file_id)

move_scf()
