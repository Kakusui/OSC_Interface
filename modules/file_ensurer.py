## built-in modules
import os
import typing

## custom modules
from handlers.file_handler import FileHandler

from modules.logger import Logger

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

   local_config_dir = os.path.join(script_dir, "LocalConfig")
   interface_dir = os.path.join(config_dir, "Interface")

   scf_host_dir = os.path.join(script_dir, "SCF")
   scf_actual_dir = os.path.join(scf_host_dir, "SCF")

   ##----------------------------------------------------------------paths----------------------------------------------------------------

   ## Local Config

   destination_dir = os.path.join(local_config_dir, "target_location.txt")
   log_path = os.path.join(local_config_dir, "log.txt")
   folder_ids_path = os.path.join(local_config_dir, "folder_ids.txt")
   folder_names_path = os.path.join(local_config_dir, "folder_names.txt")
   file_paths_path = os.path.join(local_config_dir, "file_paths.txt")
   blacklist_path = os.path.join(local_config_dir, "blacklisted_names.txt")

   ## Interface

   client_json_path = os.path.join(interface_dir, "client_secrets.json")
   last_run_path = os.path.join(interface_dir, "last_run.txt")

   Logger.log_file_path = log_path

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

      for file in [FileEnsurer.destination_dir, FileEnsurer.folder_ids_path, FileEnsurer.folder_names_path, FileEnsurer.file_paths_path, FileEnsurer.blacklist_path]:
         if(not os.path.exists(file)):
            raise FileNotFoundError(f"File {file} not found. Please ensure that the file is present and filled as specified in the documentation and try again.")


##--------------------start-of-ensure_interface_files()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def ensure_interface_files() -> None:

      """

      Ensures that the interface files are present and ready to be used.

      """

      FileHandler.standard_create_file(FileEnsurer.client_json_path)
      FileHandler.modified_create_file(FileEnsurer.last_run_path, "L")

##--------------------start-of-setup_iteration_paths()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   @staticmethod
   def setup_iteration_paths() -> None:

      """

      Sets up the iteration paths.

      """

      FileEnsurer.ids, FileEnsurer.names = FileEnsurer.get_folder_properties()

      for i, name in enumerate(FileEnsurer.names):
         FileEnsurer.dirs[i+1] = os.path.join(FileEnsurer.scf_actual_dir, name)
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

      with open(FileEnsurer.folder_ids_path, "r") as file:
         folder_ids = [line.strip() for line in file.readlines()]

      with open(FileEnsurer.folder_names_path, "r") as file:
         folder_names = [line.strip() for line in file.readlines()]

      return folder_ids, folder_names