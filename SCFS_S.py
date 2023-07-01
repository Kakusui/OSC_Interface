## built-in modules
from time import sleep 

import pyautogui as gui
import os
import shutil

## third party modules
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from ctypes import *
from apiclient import discovery
from datetime import datetime

## custom modules
from modules import util


class SCFS:

    """
    
    The SCFS class, used for backing up files.

    """

##-------------------start-of-__init__()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self) -> None: # constructor for SCFS class

        ## the folder where all the config files are located
        self.config_dir = os.path.join(os.environ['USERPROFILE'],"SCFSconfig")

        ## path to the directory where the script is located
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        self.last_run_path = os.path.join(self.config_dir, "last_run.txt")

        self.client_json_path = os.path.join(self.config_dir, "client_secrets.json")

        self.folder_ids = os.path.join(self.script_dir, "folder_ids.txt")

        self.marked_for_deletion = []

        ## the path to the usb device we are transferring to
        self.usb_path = "E:\\"

        os.system("title " + "SCFS_S.py")

        self.start_SCFS()

##-------------------start-of-start_SCFS()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def start_SCFS(self):

        if(not os.path.exists(self.usb_path)):
            print("E:\\ Does not exist\n\n")

            util.pause_console()
            exit()

        try:
            with open(self.last_run_path, "r+") as f:
                if(f.read() == datetime.now().strftime("%m/%d/%Y")):
                    print("Already ran today\n\n")

                    util.pause_console()
                    exit()
        except:
            pass

        self.setup_scf_folder()
        self.transfer()

##-------------------start-of-setup_scf_folder()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def setup_scf_folder(self):
        
        self.scf_dir = os.path.join(self.script_dir, "SCF")

        self.tafunuha_dir = os.path.join(self.scf_dir, "tafunuha")
        self.rahahinukawa_dir = os.path.join(self.scf_dir, "rahahinukawa")
        self.NuharunuNihamemekayahame_dir = os.path.join(self.scf_dir, "NuharunuNihamemekayahame")
        self.NisoMehademaRakasuni_dir = os.path.join(self.scf_dir, "NisoMehademaRakasuni")
        self.MehademaRakasuniKasunu_dir = os.path.join(self.scf_dir, "MehademaRakasuniKasunu")

        self.tafunuha_iteration_dir = os.path.join(self.tafunuha_dir, "Current Iteration")
        self.rahahinukawa_iteration_dir = os.path.join(self.rahahinukawa_dir, "Current Iteration")
        self.NuharunuNihamemekayahame_iteration_dir = os.path.join(self.NuharunuNihamemekayahame_dir, "Current Iteration")
        self.NisoMehademaRakasuni_iteration_dir = os.path.join(self.NisoMehademaRakasuni_dir, "Current Iteration")
        self.MehademaRakasuniKasunu_iteration_dir = os.path.join(self.MehademaRakasuniKasunu_dir, "Current Iteration")

        self.tafunuha_iteration_path = os.path.join(self.tafunuha_iteration_dir, "iteration.txt")
        self.rahahinukawa_iteration_path = os.path.join(self.rahahinukawa_iteration_dir, "iteration.txt")
        self.NuharunuNihamemekayahame_iteration_path = os.path.join(self.NuharunuNihamemekayahame_iteration_dir, "iteration.txt")
        self.NisoMehademaRakasuni_iteration_path = os.path.join(self.NisoMehademaRakasuni_iteration_dir, "iteration.txt")
        self.MehademaRakasuniKasunu_iteration_path = os.path.join(self.MehademaRakasuniKasunu_iteration_dir, "iteration.txt")

        util.standard_create_directory(self.scf_dir)

        util.standard_create_directory(self.tafunuha_dir)
        util.standard_create_directory(self.rahahinukawa_dir)
        util.standard_create_directory(self.NuharunuNihamemekayahame_dir)
        util.standard_create_directory(self.NisoMehademaRakasuni_dir)
        util.standard_create_directory(self.MehademaRakasuniKasunu_dir)

        util.standard_create_directory(self.tafunuha_iteration_dir)
        util.standard_create_directory(self.rahahinukawa_iteration_dir)
        util.standard_create_directory(self.NuharunuNihamemekayahame_iteration_dir)
        util.standard_create_directory(self.NisoMehademaRakasuni_iteration_dir)
        util.standard_create_directory(self.MehademaRakasuniKasunu_iteration_dir)

        util.modified_create_file(self.tafunuha_iteration_path, "1")
        util.modified_create_file(self.rahahinukawa_iteration_path, "1")
        util.modified_create_file(self.NuharunuNihamemekayahame_iteration_path, "1")
        util.modified_create_file(self.NisoMehademaRakasuni_iteration_path, "1")
        util.modified_create_file(self.MehademaRakasuniKasunu_iteration_path, "1")

##-------------------start-of-transfer()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def transfer(self):

        try:
            GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = self.client_json_path
            
            self.gauth = GoogleAuth()
            self.gauth.LocalWebserverAuth()
            self.drive = GoogleDrive(self.gauth)

        except Exception as e:
            util.clear_console()

            print("Cloud Authentication Failed Due to : " + str(e))
            
            util.pause_console()
            
            exit()

        self.download_files()

        self.move_folders()

        self.delete_files()

        currentDate = datetime.now().strftime("%m/%d/%Y")

        with open(self.last_run_path, "w+", encoding="utf-8") as file:
            file.write(currentDate)
#-------------------Start-of-download_files()-------------------------------------------------

    def download_files(self):
        
        with open(self.folder_ids, "r+", encoding="utf-8") as file:
            gfolder_ids = file.readlines()

        for i, id in enumerate(gfolder_ids):

            id = id.strip()
        
            query = "mimeType != 'application/vnd.google-apps.folder' and trashed = false and '{}' in parents".format(id)
            fileList = self.drive.ListFile({'q': query}).GetList()

            for f in fileList:
                self.marked_for_deletion.append(f['id'])

                ff = self.drive.CreateFile({'id': f['id']})

                dFile = self.get_file_path(i+1)

                print("Downloading {} as {}".format(f['title'], dFile))
                ff.GetContentFile(dFile + "." + f['fileExtension'])
                i += 1
                dFile = ""
                f = None
                ff = None


#-------------------Start-of-delete_files()-------------------------------------------------

    def delete_files(self):

        i = 0

        service = discovery.build('drive', 'v3', credentials=self.gauth.credentials)
        batch = service.new_batch_http_request(callback=None)

        for id in self.marked_for_deletion:

            id = id.strip()

            f = self.drive.CreateFile({'id':  id})

            print("Trashing {}".format(f['title']))

            batch.add(service.files().delete(fileId=f['id']))
            i += 1

        if(i != 0):
            print("Deleting Files")

        batch.execute()

#-------------------Start-of-get_file_path()-------------------------------------------------

    def get_file_path(self, Set): ## used to determine where files downloaded from the drive will go
        
        directory = datetime.today().strftime('%Y-%m-%d')

        filePaths = {
            1: self.NisoMehademaRakasuni_dir,
            2: self.MehademaRakasuniKasunu_dir,
            3: self.NuharunuNihamemekayahame_dir,
            4: self.rahahinukawa_dir,
            5: self.tafunuha_dir
        }
        iterationPaths = {
            1: self.NisoMehademaRakasuni_iteration_path,
            2: self.MehademaRakasuniKasunu_iteration_path,
            3: self.NuharunuNihamemekayahame_iteration_path,
            4: self.rahahinukawa_iteration_path,
            5: self.tafunuha_iteration_path
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

#-------------------Start-of-move_folders()-------------------------------------------------

    def move_folders(self):
        
        print("Moving Folders")

        scf2 = r'E:\SCF'

        Nuse = r'C:\Users\Tetra\Desktop\Nusevei'
        NuseBase = r'C:\Users\Tetra\Desktop\Nusevei\Nuse Backups'

        for dirpath, dirnames, filenames in os.walk(self.scf_dir):
            for filename in filenames:
                sourcePath = os.path.join(dirpath, filename)
                destinationSubDir = dirpath.split(self.scf_dir)[1]
                destinationPath = os.path.join(scf2, destinationSubDir, filename)
                if not os.path.exists(destinationPath):
                    os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
                    shutil.copy(sourcePath, destinationPath)

        for dirpath, dirnames, filenames in os.walk(Nuse):
            for filename in filenames:
                sourcePath = os.path.join(dirpath, filename)
                destinationSubDir = dirpath.split(Nuse)[1]
                destinationPath = os.path.join(self.usb_path, destinationSubDir, filename)
                if not os.path.exists(destinationPath):
                    os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
                    shutil.copy(sourcePath, destinationPath)

        shutil.rmtree(self.scf_dir)
        shutil.rmtree(NuseBase)

        sleep(.1)

        os.mkdir(NuseBase)

##-------------------start-of-main()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SCFS()