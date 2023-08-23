## built-in modules
import datetime
import os
import ctypes
import shutil

## third party modules
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient import discovery

## custom modules
from modules import util


class SCFS:

    """
    
    The SCFS class, used for backing up files.\n

    """

##-------------------start-of-__init__()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self) -> None:

        """
        
        Initializes the SCFS class.\n

        Parameters:\n
        None.\n

        Returns:\n
        None.\n

        """


        ##----------------------------------------------------------------dirs----------------------------------------------------------------

        ## the folder where all the config files are located
        self.config_dir = os.path.join(os.environ['USERPROFILE'],"SCFSconfig")

        ## path to the directory where the script is located
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        ##----------------------------------------------------------------paths----------------------------------------------------------------

        self.last_run_path = os.path.join(self.config_dir, "last_run.txt")

        self.client_json_path = os.path.join(self.config_dir, "client_secrets.json")

        self.folder_id_path = os.path.join(self.script_dir, "folder_ids.txt")

        ##----------------------------------------------------------------variables----------------------------------------------------------------

        self.marked_for_deletion = []

        ## the path to the usb device we are transferring to
        self.usb_path = "E:\\"

        #----------------------------------------------------------------run----------------------------------------------------------------

        os.system("title " + "SCFS")

        util.standard_create_directory(self.config_dir)

        util.standard_create_file(self.client_json_path)

        util.standard_create_file(self.folder_id_path)

        util.modified_create_file(self.last_run_path, "")

        self.start_SCFS()

##-------------------start-of-start_SCFS()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def start_SCFS(self) -> None:

        """
        
        Start the SCFS process.\n

        Parameters:\n
        self (object - SCFS) : the SCFS object.\n

        Returns:\n
        None.\n

        """

        ## if usb that we are transferring to does not exist than exit
        if(not os.path.exists(self.usb_path)):
            print("E:\\ Does not exist\n\n")

            util.pause_console()
            exit()

        ## no need to run multiple times a day
        with open(self.last_run_path, "r+") as f:
            if(f.read() == datetime.datetime.now().strftime("%m/%d/%Y")):
                print("Already ran today\n")

                util.pause_console()
                exit()

        self.transfer()

##-------------------start-of-transfer()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def transfer(self) -> None:

        """
        
        Begins the transfer process.\n

        Parameters:\n
        self (object - SCFS) : the SCFS object.\n

        Returns:\n
        None.\n

        """

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

        # Get the handle of the console window
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()

        # Maximize the console window
        ctypes.windll.user32.ShowWindow(hwnd, 6)

        util.clear_console()

        self.setup_scf_folder()

        self.download_files()

        self.move_folders()

        self.delete_files()

        currentDate = datetime.datetime.now().strftime("%m/%d/%Y")

        with open(self.last_run_path, "w+", encoding="utf-8") as file:
            file.write(currentDate)

##-------------------start-of-setup_scf_folder()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def setup_scf_folder(self) -> None:

        """
        
        Setups the scf folder.\n

        Parameters:\n
        self (object - SCFS) : the SCFS object.\n

        Returns:\n
        None.\n

        """
        
        self.scf_dir = os.path.join(self.script_dir, "SCF")
        self.scf_actual_dir = os.path.join(self.scf_dir, "SCF")

        self.tafunuha_dir = os.path.join(self.scf_actual_dir, "tafunuha")
        self.rahahinukawa_dir = os.path.join(self.scf_actual_dir, "rahahinukawa")
        self.NuharunuNihamemekayahame_dir = os.path.join(self.scf_actual_dir, "NuharunuNihamemekayahame")
        self.NisoMehademaRakasuni_dir = os.path.join(self.scf_actual_dir, "NisoMehademaRakasuni")
        self.MehademaRakasuniKasunu_dir = os.path.join(self.scf_actual_dir, "MehademaRakasuniKasunu")
        self.TaninMehademaRakasuni_dir = os.path.join(self.scf_actual_dir, "TaninMehademaRakasuni")

        self.tafunuha_iteration_dir = os.path.join(self.tafunuha_dir, "Current Iteration")
        self.rahahinukawa_iteration_dir = os.path.join(self.rahahinukawa_dir, "Current Iteration")
        self.NuharunuNihamemekayahame_iteration_dir = os.path.join(self.NuharunuNihamemekayahame_dir, "Current Iteration")
        self.NisoMehademaRakasuni_iteration_dir = os.path.join(self.NisoMehademaRakasuni_dir, "Current Iteration")
        self.MehademaRakasuniKasunu_iteration_dir = os.path.join(self.MehademaRakasuniKasunu_dir, "Current Iteration")
        self.TaninMehademaRakasuni_iteration_dir = os.path.join(self.TaninMehademaRakasuni_dir, "Current Iteration")

        self.tafunuha_iteration_path = os.path.join(self.tafunuha_iteration_dir, "iteration.txt")
        self.rahahinukawa_iteration_path = os.path.join(self.rahahinukawa_iteration_dir, "iteration.txt")
        self.NuharunuNihamemekayahame_iteration_path = os.path.join(self.NuharunuNihamemekayahame_iteration_dir, "iteration.txt")
        self.NisoMehademaRakasuni_iteration_path = os.path.join(self.NisoMehademaRakasuni_iteration_dir, "iteration.txt")
        self.MehademaRakasuniKasunu_iteration_path = os.path.join(self.MehademaRakasuniKasunu_iteration_dir, "iteration.txt")
        self.TaninMehademaRakasuni_iteration_path = os.path.join(self.TaninMehademaRakasuni_iteration_dir, "iteration.txt")

        util.standard_create_directory(self.scf_dir)

        util.standard_create_directory(self.scf_actual_dir)

        util.standard_create_directory(self.tafunuha_dir)
        util.standard_create_directory(self.rahahinukawa_dir)
        util.standard_create_directory(self.NuharunuNihamemekayahame_dir)
        util.standard_create_directory(self.NisoMehademaRakasuni_dir)
        util.standard_create_directory(self.MehademaRakasuniKasunu_dir)
        util.standard_create_directory(self.TaninMehademaRakasuni_dir)

        util.standard_create_directory(self.tafunuha_iteration_dir)
        util.standard_create_directory(self.rahahinukawa_iteration_dir)
        util.standard_create_directory(self.NuharunuNihamemekayahame_iteration_dir)
        util.standard_create_directory(self.NisoMehademaRakasuni_iteration_dir)
        util.standard_create_directory(self.MehademaRakasuniKasunu_iteration_dir)
        util.standard_create_directory(self.TaninMehademaRakasuni_iteration_dir)

        util.modified_create_file(self.tafunuha_iteration_path, "1")
        util.modified_create_file(self.rahahinukawa_iteration_path, "1")
        util.modified_create_file(self.NuharunuNihamemekayahame_iteration_path, "1")
        util.modified_create_file(self.NisoMehademaRakasuni_iteration_path, "1")
        util.modified_create_file(self.MehademaRakasuniKasunu_iteration_path, "1")
        util.modified_create_file(self.TaninMehademaRakasuni_iteration_path, "1")

#-------------------Start-of-download_files()-------------------------------------------------

    def download_files(self) -> None:

        """
        
        Downloads all files in a google drive folder.\n

        Parameters:\n
        self (object - SCFS) : the SCFS object.\n

        Returns:\n
        None.\n

        """
        
        with open(self.folder_id_path, "r+", encoding="utf-8") as file:
            gfolder_ids = file.readlines()

        for i, id in enumerate(gfolder_ids):

            if(i >= 6):
                break

            id = id.strip()
            query = "mimeType != 'application/vnd.google-apps.folder' and trashed = false and '{}' in parents".format(id)
            fileList = self.drive.ListFile({'q': query}).GetList()

            for f in fileList:
                self.marked_for_deletion.append(f['id'])

                ff = self.drive.CreateFile({'id': f['id']})

                file_path = self.get_file_path(i + 1)

                print("Downloading {} as {}".format(f['title'], file_path))
                ff.GetContentFile(file_path + "." + f['fileExtension'])

                file_path = ""
                f = None
                ff = None


#-------------------Start-of-delete_files()-------------------------------------------------

    def delete_files(self) -> None:

        """
        
        Deletes all files that have been marked for deletion.\n

        Parameters:\n
        self (object - SCFS) : the SCFS object.\n

        Returns:\n
        None.\n

        """

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

    def get_file_path(self, file_type) -> str:

        """
        
        Gets a new file path for a downloaded file.\n

        Parameters:\n
        self (object - SCFS) : the SCFS object.\n

        Returns:\n
        None.\n

        """ 
        
        directory = datetime.datetime.today().strftime('%Y-%m-%d')

        filePaths = {
            1: self.NisoMehademaRakasuni_dir,
            2: self.MehademaRakasuniKasunu_dir,
            3: self.NuharunuNihamemekayahame_dir,
            4: self.rahahinukawa_dir,
            5: self.tafunuha_dir,
            6: self.TaninMehademaRakasuni_dir
        }
        iterationPaths = {
            1: self.NisoMehademaRakasuni_iteration_path,
            2: self.MehademaRakasuniKasunu_iteration_path,
            3: self.NuharunuNihamemekayahame_iteration_path,
            4: self.rahahinukawa_iteration_path,
            5: self.tafunuha_iteration_path,
            6: self.TaninMehademaRakasuni_iteration_path
        }
        
        path = os.path.join(filePaths[file_type], directory)

        with open(iterationPaths[file_type], "r", encoding="utf8") as f:
            Iteration = int(f.read())

        os.makedirs(path, exist_ok=True)
        
        file_path = path + "/" + directory + "-" + str(Iteration)
        Iteration += 1

        with open(iterationPaths[file_type], "w", encoding="utf8") as f:
            f.write(str(Iteration))

        return file_path

##-------------------start-of-move_folders()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def move_folders(self) -> None:

        """
        
        Transfers all downloaded files to the designated usb.\n

        Parameters:\n
        self (object - SCFS) : the SCFS object.\n

        Returns:\n
        None.\n

        """

        ## destination folder for the scf folder
        destination_scf = os.path.join(os.path.join(self.usb_path, "SCF"), "SCF")

        ## the paths to the usb device we are transferring to for seinu and nuse
        usb_nuse = os.path.join(self.usb_path, "Nuse Backups")
        usb_seinu = os.path.join(self.usb_path, "Seinu")

        ## folder for the where the backups folder is
        nusevei_backups = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"),"Nusevei")

        ## backups folder for the sal files
        nusevei_backup_actual = os.path.join(nusevei_backups, "Nuse Backups")

        ## main seinu folder
        seinu_backups = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"),"Seinu")
        
        print("Merging SCF Folders")

        self.merge_directories(self.scf_actual_dir, destination_scf, overwrite=True)

        print("Merging Nuse Folders")

        self.merge_directories(nusevei_backup_actual, usb_nuse, overwrite=True)

        print("Merging Seinu Folder")

        self.merge_directories(seinu_backups, usb_seinu, overwrite=True)

        try:
            shutil.rmtree(self.scf_dir)

        except:
            pass

        try:
            shutil.rmtree(nusevei_backup_actual)

        except:
            pass

##-------------------start-of-merge_directories()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def merge_directories(self, source_directory, destination_directory, overwrite=False) -> None:

        """

        Merge the contents of the source directory into the destination directory.\n

        Parameters:\n
        source_directory (str): The source directory path.\n
        destination_directory (str): The destination directory path.\n
        overwrite (bool): If True, overwrite existing files in the destination directory (default is False).\n

        Returns:\n
        None.\n

        """

        for item in os.listdir(source_directory):
            source_item = os.path.join(source_directory, item)
            destination_item = os.path.join(destination_directory, item)

            if(os.path.isfile(source_item)):
                if os.path.exists(destination_item) and not overwrite:
                    continue  # Skip if the file already exists in the destination directory
                os.makedirs(os.path.dirname(destination_item), exist_ok=True)  # Create parent directories if necessary
                shutil.copy2(source_item, destination_item)
                
            elif(os.path.isdir(source_item)):
                if(os.path.exists(destination_item) and overwrite):
                    if(os.path.isdir(destination_item)):
                        shutil.rmtree(destination_item)  # Remove existing directory
                    else:
                        os.remove(destination_item)  # Remove existing file
                shutil.copytree(source_item, destination_item, copy_function=shutil.copy2)

##-------------------start-of-main()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SCFS()