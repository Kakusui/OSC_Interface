## built-in libraries
import datetime
import os
import shutil


## third party libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient import discovery
from googleapiclient.http import BatchHttpRequest

## custom modules
from modules.file_ensurer import FileEnsurer
from modules.toolkit import Toolkit

from handlers.file_handler import FileHandler


class Interface:

    """

    Used for interfacing with the OSC.

    """

    marked_for_deletion = []

    gauth:GoogleAuth
    drive:GoogleDrive

##-------------------start-of-start_interaction()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def start_interaction() -> None:

        """
        
        Start the interaction with OSC.

        """


        os.system("title " + "OSC Interface")

        FileEnsurer.ensure_files()

        FileEnsurer.setup_iteration_paths()

        ## if usb that we are transferring to does not exist than exit
        if(not os.path.exists(FileEnsurer.usb_path)):
            print(FileEnsurer.usb_path + " Does not exist\n")

            Toolkit.pause_console()
            exit()

        ## no need to run multiple times a day
        with open(FileEnsurer.last_run_path, "r+") as f:
            if(f.read() == datetime.datetime.now().strftime("%m/%d/%Y")):
                print("Already ran today\n")

                Toolkit.pause_console()
                exit()

        Interface.transfer()

##-------------------start-of-transfer()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def transfer() -> None:

        """
        
        Begins the transfer process.

        """

        try:
            GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = FileEnsurer.client_json_path
            
            Interface.gauth = GoogleAuth()
            Interface.gauth.LocalWebserverAuth()
            Interface.drive = GoogleDrive(Interface.gauth)

        except Exception as e:
            Toolkit.clear_console()

            print("Cloud Authentication Failed Due to : " + str(e))
            
            Toolkit.pause_console()
            
            exit()

        Toolkit.clear_console()

        Interface.setup_scf_folder()

        Interface.download_files()

        Interface.move_folders()

        Interface.delete_files()

        currentDate = datetime.datetime.now().strftime("%m/%d/%Y")

        with open(FileEnsurer.last_run_path, "w+", encoding="utf-8") as file:
            file.write(currentDate)

##-------------------start-of-setup_scf_folder()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def setup_scf_folder() -> None:

        """
        
        Setups the scf folder.

        """

        FileHandler.standard_create_directory(FileEnsurer.scf_host_dir)
        FileHandler.standard_create_directory(FileEnsurer.scf_actual_dir)
        
        for path in FileEnsurer.dirs.values():
            FileHandler.standard_create_directory(path)

        for path in FileEnsurer.iteration_dirs.values():
            FileHandler.standard_create_directory(path)

        for path in FileEnsurer.iteration_paths.values():
            FileHandler.modified_create_file(path, "1")
        
##-------------------start-of-download_files()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def download_files() -> None:

        """
        
        Downloads all files in a google drive folder.

        """

        for i, id in enumerate(FileEnsurer.ids):

            if(i >= 6):
                break

            id = id.strip()
            query = "mimeType != 'application/vnd.google-apps.folder' and trashed = false and '{}' in parents".format(id)
            fileList = Interface.drive.ListFile({'q': query}).GetList()

            for drive_file in fileList:
                Interface.marked_for_deletion.append(drive_file['id'])

                downloaded_file = Interface.drive.CreateFile({'id': drive_file['id']})

                file_path = Interface.get_file_path(i + 1)

                print("Downloading {} as {}".format(downloaded_file['title'], file_path + "." + drive_file['fileExtension']))
                downloaded_file.GetContentFile(file_path + "." + drive_file['fileExtension'])

##-------------------start-of-delete_files()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def delete_files() -> None:

        """
        
        Deletes all files that have been marked for deletion.

        """

        i = 0

        service = discovery.build('drive', 'v3', credentials=Interface.gauth.credentials)
        batch:BatchHttpRequest = service.new_batch_http_request()

        for id in Interface.marked_for_deletion:

            id = id.strip()

            f = Interface.drive.CreateFile({'id':  id})

            print("Trashing {}".format(f['title']))

            batch.add(service.files().delete(fileId=f['id']))
            i += 1

        if(i != 0):
            print("Deleting Files")

        batch.execute()

#-------------------Start-of-get_file_path()-------------------------------------------------

    @staticmethod
    def get_file_path(file_type:int) -> str:

        """
        
        Gets a new file path for a downloaded file.

        """ 
        
        directory = datetime.datetime.today().strftime('%Y-%m-%d')
        
        path = os.path.join(FileEnsurer.dirs[file_type], directory)

        with open(FileEnsurer.iteration_paths[file_type], "r", encoding="utf8") as f:
            iteration = int(f.read())

        os.makedirs(path, exist_ok=True)
        
        file_path = path + "/" + directory + "-" + str(iteration)
        iteration += 1

        while True:

            try:

                with open(FileEnsurer.iteration_paths[file_type], "w", encoding="utf8") as f:
                    f.write(str(iteration))

                break

            except PermissionError:
                pass

        return file_path

##-------------------start-of-move_folders()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def move_folders() -> None:

        """
        
        Transfers all downloaded files to the designated usb.

        """

        with open(FileEnsurer.file_names_path , "r+", encoding="utf-8") as file:
            filenames = file.readlines()

        with open(FileEnsurer.blacklist_path , "r+", encoding="utf-8") as file:
            blacklist = file.readlines()

        ## destination folder for the scf folder
        destination_scf = os.path.join(FileEnsurer.usb_path, "SCF")

        ## the paths to the usb device we are transferring to for user and data
        destination_database_backups = os.path.join(FileEnsurer.usb_path, filenames[0].strip() + " Backups")
        destination_user_dir = os.path.join(FileEnsurer.usb_path, filenames[1].strip())

        ## folder for the where the backups folder is
        src_database_backups_dir = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"),filenames[0].strip())

        ## backups folder for the database files
        database_backup_actual = os.path.join(src_database_backups_dir, f"{filenames[0].strip()} Backups")

        ## main user folder
        desktop_user_directory = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"), filenames[1].strip())
        
        print("Merging SCF Folders")

        Interface.merge_directories(FileEnsurer.scf_actual_dir, destination_scf, overwrite=True)

        print(f"Merging {filenames[0].strip()} Folders")

        Interface.merge_directories(database_backup_actual, destination_database_backups, overwrite=True)

        print(f"Merging {filenames[1].strip()} Folders")

        try:
            shutil.rmtree(destination_user_dir)
            os.mkdir(destination_user_dir)

        except:
            pass

        Interface.merge_directories(desktop_user_directory, destination_user_dir, overwrite=True, blacklist_directories=blacklist)

        try:
            shutil.rmtree(FileEnsurer.scf_host_dir)

        except:
            pass

        try:
            shutil.rmtree(database_backup_actual)
            os.mkdir(database_backup_actual)

        except:
            pass
        
##-------------------start-of-merge_directories()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def merge_directories(source_directory, destination_directory, overwrite=False, blacklist_directories=[]) -> None:

        """

        Merge the contents of the source directory into the destination directory.

        Parameters:\n
        source_directory (str) : The source directory path.
        destination_directory (str) : The destination directory path.
        overwrite (bool | optional | default=False) : If True, overwrite existing files but not directories in the destination directory.

        """

        for item in os.listdir(source_directory):
            source_item = os.path.join(source_directory, item)
            destination_item = os.path.join(destination_directory, item)

            if(os.path.isfile(source_item)):

                if(os.path.exists(destination_item) and not overwrite):
                    continue  ## Skip if the file already exists in the destination directory

                os.makedirs(os.path.dirname(destination_item), exist_ok=True)  ## Create parent directories if necessary
                shutil.copy2(source_item, destination_item)

            elif(os.path.isdir(source_item)):

                if(item in blacklist_directories):
                    continue

                if(os.path.exists(destination_item) and not overwrite):
                    ## Merge the contents of the source directory into the existing destination directory
                    Interface.merge_directories(source_item, destination_item, overwrite)
                else:
                    ## If destination directory doesn't exist, create it and copy the contents
                    os.makedirs(destination_item, exist_ok=True)
                    Interface.merge_directories(source_item, destination_item, overwrite)

##-------------------start-of-main()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Interface.start_interaction()