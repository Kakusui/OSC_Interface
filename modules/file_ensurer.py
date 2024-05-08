## built-in modules
import os
import typing

## custom modules
from handlers.file_handler import FileHandler

class FileEnsurer:

   """
   
   The FileEnsurer class is used to ensure that the files needed to run the program are present and ready to be used.

   """

   ##----------------------------------------------------------------dirs----------------------------------------------------------------

   script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

   if(os.name == 'nt'):  ## Windows
      config_dir = os.path.join(os.environ['USERPROFILE'],"OSCInterfaceConfig")
   else:  ## Linux
      config_dir = os.path.join(os.path.expanduser("~"), "OSCInterfaceConfig")

   local_config_dir = os.path.join(script_dir, "localconfig")
   interface_dir = os.path.join(config_dir, "interface")

   with open(os.path.join(local_config_dir, "downloaded_files_directory_name.txt"), "r") as file:
      downloaded_files_directory_name = file.read().strip()

   local_downloaded_files_host_dir = os.path.join(script_dir, downloaded_files_directory_name)
   local_downloaded_files_actual_dir = os.path.join(local_downloaded_files_host_dir, downloaded_files_directory_name)

   ##----------------------------------------------------------------paths----------------------------------------------------------------

   ## Local Config

   target_location_path = os.path.join(local_config_dir, "target_location.txt")
   google_folder_ids_file_path = os.path.join(local_config_dir, "google_folder_ids.txt")
   google_folder_names_file_path = os.path.join(local_config_dir, "google_folder_names.txt")
   transfer_file_paths = os.path.join(local_config_dir, "file_paths_to_transfer.txt")

   ## Interface

   client_json_path = os.path.join(interface_dir, "client_secrets.json")

   ##----------------------------------------------------------------variables----------------------------------------------------------------

   ids = []
   names = []

   dirs:typing.Dict[int,str] = {}
   iteration_dirs:typing.Dict[int,str] = {}
   iteration_paths:typing.Dict[int,str] = {}

##--------------------start-of-ensure_files()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def ensure_files() -> None:

      """

      This function ensures that the files needed to run the program are present and ready to be used.
            
      """


      try:
         os.mkdir(FileEnsurer.config_dir)
      except:
         pass

      FileEnsurer.create_needed_base_directories()
      FileEnsurer.ensure_local_config_files()
      FileEnsurer.ensure_interface_files()

##--------------------start-of-create_needed_base_directories()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def create_needed_base_directories() -> None:

      """
      
      Creates the needed base directories.
      
      """

      FileHandler.standard_create_directory(FileEnsurer.local_config_dir)
      FileHandler.standard_create_directory(FileEnsurer.interface_dir)

##--------------------start-of-ensure_local_config_files()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def ensure_local_config_files() -> None:

      """
      
      Ensures that the local config files are present and ready to be used.

      """

      for file in [FileEnsurer.target_location_path, 
                   FileEnsurer.google_folder_ids_file_path, 
                   FileEnsurer.google_folder_names_file_path, 
                   FileEnsurer.transfer_file_paths]:
         
         if(not os.path.exists(file)):
            raise FileNotFoundError(f"File {file} not found. Please ensure that the file is present and filled as specified in the documentation and try again.")

##--------------------start-of-ensure_interface_files()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def ensure_interface_files() -> None:

      """

      Ensures that the interface files are present and ready to be used.

      """

      assert os.path.exists(FileEnsurer.client_json_path), f"File {FileEnsurer.client_json_path} not found. Please contact Kakusui to be issued a new client_secrets.json file at contact@kakusui.org."

##--------------------start-of-setup_iteration_paths()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def setup_iteration_paths() -> None:

      """

      Sets up the iteration paths.

      """

      FileEnsurer.ids, FileEnsurer.names = FileEnsurer.get_folder_properties()

      for i, name in enumerate(FileEnsurer.names):
         FileEnsurer.dirs[i+1] = os.path.join(FileEnsurer.local_downloaded_files_host_dir, name)
         FileEnsurer.iteration_dirs[i+1] = os.path.join(FileEnsurer.dirs[i+1], "current_iteration")
         FileEnsurer.iteration_paths[i+1] = os.path.join(FileEnsurer.iteration_dirs[i+1], "iteration.txt")

##--------------------start-of-get_folder_properties()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def get_folder_properties() -> typing.Tuple[typing.List[str], typing.List[str]]:

      """

      Gets the folder properties from the local config files.

      Returns:
      folder_ids (list - str) : the folder ids.
      folder_names (list - str) : the folder names.
      
      """

      with open(FileEnsurer.google_folder_ids_file_path, "r") as file:
         folder_ids = [line.strip() for line in file.readlines()]

      with open(FileEnsurer.google_folder_names_file_path, "r") as file:
         folder_names = [line.strip() for line in file.readlines()]

      return folder_ids, folder_names