## built-in libraries
import datetime
import os
import shutil
import logging

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

    Used for interfacing with the OSC (Okisouchi)

    """

    google_folder_ids_marked_for_deletion = []

    gauth:GoogleAuth
    drive:GoogleDrive

    destination:str

##-------------------start-of-start_interaction()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def start_interaction() -> None:

        """
        
        Start the interaction with OSC.

        """


        os.system("title " + "OSC Interface")

        FileEnsurer.ensure_files()

        FileEnsurer.setup_iteration_paths()

        Interface.destination = FileHandler.standard_read_file(FileEnsurer.target_location_path)

        ## if destination that we are transferring to does not exist than exit
        if(not os.path.exists(Interface.destination)):
            print(Interface.destination + " Does not exist\n")

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

        Interface.setup_local_download_folder_storage()

        Interface.download_files()

        Interface.move_folders()

        Interface.delete_files()

##-------------------start-of-setup_local_download_folder_storage()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def setup_local_download_folder_storage() -> None:

        """
        
        Setups the local download folder storage.

        """

        FileHandler.standard_create_directory(FileEnsurer.local_downloaded_files_host_dir)
        FileHandler.standard_create_directory(FileEnsurer.local_downloaded_files_actual_dir)
        
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


            id = id.strip()
            query = "mimeType != 'application/vnd.google-apps.folder' and trashed = false and '{}' in parents".format(id)
            fileList = Interface.drive.ListFile({'q': query}).GetList()

            for drive_file in fileList:
        
                downloaded_file = Interface.drive.CreateFile({'id': drive_file['id']})

                file_path = Interface.get_file_path(i + 1)

                logging.info("Downloading {} as {}".format(downloaded_file['title'], file_path + "." + drive_file['fileExtension']))

                downloaded_file.GetContentFile(file_path + "." + drive_file['fileExtension'])

                Interface.google_folder_ids_marked_for_deletion.append(drive_file['id'])
                logging.info("Marking {} for deletion".format(downloaded_file['title']))

##-------------------start-of-delete_files()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def delete_files() -> None:

        """
        
        Deletes all files that have been marked for deletion.

        """

        i = 0

        service = discovery.build('drive', 'v3', credentials=Interface.gauth.credentials)
        batch:BatchHttpRequest = service.new_batch_http

        for id in Interface.google_folder_ids_marked_for_deletion:

            id = id.strip()

            f = Interface.drive.CreateFile({'id':  id})

            logging.info("Trashing {}".format(f['title']))

            batch.add(service.files().delete(fileId=f['id']))
            i += 1

        if(i != 0):
            logging.info("Deleting {} files".format(i))
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
                logging.warning(f"Permission Error: {file_path} cannot be accessed")
                pass

        return file_path

##-------------------start-of-move_folders()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def move_folders() -> None:

        """
        
        Transfers all downloaded files to the designated usb.

        """

        with open(FileEnsurer.transfer_file_paths , "r+", encoding="utf-8") as file:
            folders_to_copy = file.readlines()

        ## destination folder for the downloaded files
        downloaded_folders_destination_path = os.path.join(Interface.destination, FileEnsurer.downloaded_files_directory_name)

        if(not os.path.exists(downloaded_folders_destination_path)):
            os.mkdir(downloaded_folders_destination_path)

        logging.info("Merging Files from Local to Destination")

        Interface.merge_directories(FileEnsurer.local_downloaded_files_actual_dir, downloaded_folders_destination_path, overwrite=True)


        for folder_path in folders_to_copy:
            folder_path = folder_path.strip()

            folder_name = os.path.basename(folder_path)

            destination_folder = os.path.join(Interface.destination, folder_name)

            Interface.merge_directories(folder_path, destination_folder, overwrite=True)

        ## gets rid of the files we just copied
        try:
            shutil.rmtree(FileEnsurer.local_downloaded_files_host_dir)
        except:
            pass
##-------------------start-of-merge_directories()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def merge_directories(source_directory, destination_directory, overwrite=False) -> None:

        """

        Merge the contents of the source directory into the destination directory.

        Parameters:
        source_directory (str) : the source directory path.
        destination_directory (str) : the destination directory path.
        overwrite (bool | optional | default=False) : if true, overwrite existing files but not directories in the destination directory.
        blacklist_directories (list | optional | default=[]) : list of directory names to ignore during the merge.

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

                if(os.path.exists(destination_item) and not overwrite):
                    ## Merge the contents of the source directory into the existing destination directory
                    Interface.merge_directories(source_item, destination_item, overwrite)
                else:
                    ## If destination directory doesn't exist, create it and copy the contents
                    os.makedirs(destination_item, exist_ok=True)
                    Interface.merge_directories(source_item, destination_item, overwrite)

##-------------------start-of-main()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## setup logging
logging.basicConfig(level=logging.DEBUG, 
                    filename='osc_interface.log', 
                    filemode='w', 
                    format='[%(asctime)s] [%(levelname)s] [%(filename)s] %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

Interface.start_interaction()