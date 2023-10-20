## built-in libraries
import datetime
import os
import shself.toolkit

## third party libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient import discovery

## custom modules
from modules.fileEnsurer import fileEnsurer
from modules.toolkit import toolkit

class Interface:

    """

    Used for interfacing with the OSC.\n

    """

##-------------------start-of-__init__()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self) -> None:

        """
        
        Initializes the Interface class.\n

        Parameters:\n
        None.\n

        Returns:\n
        None.\n

        """

        ##--------------------------------------------------------------objects----------------------------------------------------------------

        self.file_ensurer = fileEnsurer()

        self.toolkit = toolkit(self.file_ensurer.logger)

        ##----------------------------------------------------------------variables----------------------------------------------------------------

        self.marked_for_deletion = []

        #----------------------------------------------------------------run----------------------------------------------------------------

        os.system("title " + "OSC Interface")

        self.file_ensurer.ensure_files()

        self.start_interaction()

##-------------------start-of-start_interaction()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def start_interaction(self) -> None:

        """
        
        Start the interaction with OSC.\n

        Parameters:\n
        self (object - Interface) : the Interface object.\n

        Returns:\n
        None.\n

        """

        ## if usb that we are transferring to does not exist than exit
        if(not os.path.exists(self.file_ensurer.usb_path)):
            print("E:\\ Does not exist\n")

            self.toolkit.pause_console()
            exit()

        ## no need to run multiple times a day
        with open(self.file_ensurer.last_run_path, "r+") as f:
            if(f.read() == datetime.datetime.now().strftime("%m/%d/%Y")):
                print("Already ran today\n")

                self.toolkit.pause_console()
                exit()

        self.transfer()

##-------------------start-of-transfer()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def transfer(self) -> None:

        """
        
        Begins the transfer process.\n

        Parameters:\n
        self (object - Interface) : the Interface object.\n

        Returns:\n
        None.\n

        """

        try:
            GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = self.file_ensurer.client_json_path
            
            self.gauth = GoogleAuth()
            self.gauth.LocalWebserverAuth()
            self.drive = GoogleDrive(self.gauth)

        except Exception as e:
            self.toolkit.clear_console()

            print("Cloud Authentication Failed Due to : " + str(e))
            
            self.toolkit.pause_console()
            
            exit()

        self.toolkit.clear_console()

        self.setup_scf_folder()

        self.download_files()

        self.move_folders()

        self.delete_files()

        currentDate = datetime.datetime.now().strftime("%m/%d/%Y")

        with open(self.file_ensurer.last_run_path, "w+", encoding="utf-8") as file:
            file.write(currentDate)

##-------------------start-of-setup_scf_folder()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def setup_scf_folder(self) -> None:

        """
        
        Setups the scf folder.\n

        Parameters:\n
        self (object - Interface) : the Interface object.\n

        Returns:\n
        None.\n

        """
        
        self.scf_host_dir = os.path.join(self.file_ensurer.script_dir, "SCF")
        self.scf_actual_dir = os.path.join(self.scf_host_dir, "SCF")

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

        self.toolkit.standard_create_directory(self.scf_host_dir)

        self.toolkit.standard_create_directory(self.scf_actual_dir)

        self.toolkit.standard_create_directory(self.tafunuha_dir)
        self.toolkit.standard_create_directory(self.rahahinukawa_dir)
        self.toolkit.standard_create_directory(self.NuharunuNihamemekayahame_dir)
        self.toolkit.standard_create_directory(self.NisoMehademaRakasuni_dir)
        self.toolkit.standard_create_directory(self.MehademaRakasuniKasunu_dir)
        self.toolkit.standard_create_directory(self.TaninMehademaRakasuni_dir)

        self.toolkit.standard_create_directory(self.tafunuha_iteration_dir)
        self.toolkit.standard_create_directory(self.rahahinukawa_iteration_dir)
        self.toolkit.standard_create_directory(self.NuharunuNihamemekayahame_iteration_dir)
        self.toolkit.standard_create_directory(self.NisoMehademaRakasuni_iteration_dir)
        self.toolkit.standard_create_directory(self.MehademaRakasuniKasunu_iteration_dir)
        self.toolkit.standard_create_directory(self.TaninMehademaRakasuni_iteration_dir)

        self.toolkit.modified_create_file(self.tafunuha_iteration_path, "1")
        self.toolkit.modified_create_file(self.rahahinukawa_iteration_path, "1")
        self.toolkit.modified_create_file(self.NuharunuNihamemekayahame_iteration_path, "1")
        self.toolkit.modified_create_file(self.NisoMehademaRakasuni_iteration_path, "1")
        self.toolkit.modified_create_file(self.MehademaRakasuniKasunu_iteration_path, "1")
        self.toolkit.modified_create_file(self.TaninMehademaRakasuni_iteration_path, "1")
        
#-------------------Start-of-download_files()-------------------------------------------------

    def download_files(self) -> None:

        """
        
        Downloads all files in a google drive folder.\n

        Parameters:\n
        self (object - Interface) : the Interface object.\n

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
        self (object - Interface) : the Interface object.\n

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
        self (object - Interface) : the Interface object.\n

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
        self (object - Interface) : the Interface object.\n

        Returns:\n
        None.\n

        """

        with open(r"filenames.txt" , "r+", encoding="utf-8") as file:
            filenames = file.readlines()

        ## destination folder for the scf folder
        destination_scf = os.path.join(self.usb_path, "SCF")

        ## the paths to the usb device we are transferring to for user and data
        destination_database_backups = os.path.join(self.usb_path, filenames[0].strip() + " Backups")
        destination_user_dir = os.path.join(self.usb_path, filenames[1].strip())

        ## folder for the where the backups folder is
        src_database_backups_dir = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"),filenames[0].strip())

        ## backups folder for the database files
        database_backup_actual = os.path.join(src_database_backups_dir, f"{filenames[0].strip()} Backups")

        ## main user folder
        desktop_user_directory = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"), filenames[1].strip())
        
        print("Merging SCF Folders")

        self.merge_directories(self.scf_actual_dir, destination_scf, overwrite=True)

        print(f"Merging {filenames[0].strip()} Folders")

        self.merge_directories(database_backup_actual, destination_database_backups, overwrite=True)

        print(f"Merging {filenames[1].strip()} Folders")

        try:
            shself.toolkit.rmtree(destination_user_dir)
            os.mkdir(destination_user_dir)

        except:
            pass

        self.merge_directories(desktop_user_directory, destination_user_dir, overwrite=True)

        try:
            shself.toolkit.rmtree(self.scf_host_dir)

        except:
            pass

        try:
            shself.toolkit.rmtree(database_backup_actual)
            os.mkdir(database_backup_actual)

        except:
            pass
        

##-------------------start-of-merge_directories()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def merge_directories(self, source_directory, destination_directory, overwrite=False) -> None:

        """

        Merge the contents of the source directory into the destination directory.\n

        Parameters:\n
        source_directory (str) : The source directory path.\n
        destination_directory (str) : The destination directory path.\n
        overwrite (bool | optional) : If True, overwrite existing files but not directories in the destination directory (default is False).\n

        Returns:\n
        None.\n

        """

        for item in os.listdir(source_directory):
            source_item = os.path.join(source_directory, item)
            destination_item = os.path.join(destination_directory, item)

            if(os.path.isfile(source_item)):

                if(os.path.exists(destination_item) and not overwrite):
                    continue  ## Skip if the file already exists in the destination directory

                os.makedirs(os.path.dirname(destination_item), exist_ok=True)  ## Create parent directories if necessary
                shself.toolkit.copy2(source_item, destination_item)

            elif(os.path.isdir(source_item)):

                if(os.path.exists(destination_item) and not overwrite):
                    ## Merge the contents of the source directory into the existing destination directory
                    self.merge_directories(source_item, destination_item, overwrite)
                else:
                    ## If destination directory doesn't exist, create it and copy the contents
                    os.makedirs(destination_item, exist_ok=True)
                    self.merge_directories(source_item, destination_item, overwrite)

##-------------------start-of-main()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Interface()