## built-in modules
from datetime import datetime, timedelta

import os
import typing

## custom modules
from handlers.fileHandler import fileHandler

from modules.logger import logger

class fileEnsurer:

   """
   
   The fileEnsurer class is used to ensure that the files needed to run the program are present and ready to be used.\n

   """

##--------------------start-of-__init__()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   def __init__(self) -> None:

      """
      
      Initializes the fileEnsurer class.\n

      Parameters:\n
      None.\n

      Returns:\n
      None.\n

      """
   

      ##----------------------------------------------------------------dirs----------------------------------------------------------------

      self.script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

      if(os.name == 'nt'):  ## Windows
         self.config_dir = os.path.join(os.environ['USERPROFILE'],"OSCInterfaceConfig")
      else:  ## Linux
         self.config_dir = os.path.join(os.path.expanduser("~"), "OSCInterfaceConfig")

      self.local_config_dir = os.path.join(self.script_dir, "LocalConfig")
      self.interface_dir = os.path.join(self.config_dir, "Interface")

      ##----------------------------------------------------------------paths----------------------------------------------------------------

      ## log file

      self.log_path = os.path.join(self.local_config_dir, "log.txt")

      ##----------------------------------------------------------------functions----------------------------------------------------------------

      ## makes config dir where log sits, if not already there

      try:
         os.mkdir(self.config_dir)
      except:
         pass

      ##----------------------------------------------------------------objects----------------------------------------------------------------

      ## logger for all actions taken by Seisen.\n
      self.logger = logger(self.log_path)

      self.file_handler = fileHandler(self.logger)

##--------------------start-of-ensure_files()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   async def ensure_files(self) -> None:

      """

      This function ensures that the files needed to run the program are present and ready to be used.\n
      
      Parameters:\n
      self (object - fileEnsurer) : the fileEnsurer object.\n

      Returns:\n
      None.\n
      
      """

      self.create_needed_base_directories()
      self.ensure_local_config_files()

##--------------------start-of-create_needed_base_directories()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   def create_needed_base_directories(self) -> None:

      """
      
      Creates the needed base directories.\n

      Parameters:\n
      self (object - fileEnsurer) : the fileEnsurer object.\n

      Returns:\n
      None.\n
      
      """

      self.file_handler.standard_create_directory(self.local_config_dir)
      self.file_handler.standard_create_directory(self.interface_dir)

##--------------------start-of-ensure_local_config_files()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   def ensure_local_config_files(self) -> None:

      """
      
      Ensures that the local config files are present and ready to be used.\n

      Parameters:\n
      self (object - fileEnsurer) : the fileEnsurer object.\n

      Returns:\n
      None.\n
      
      """

      util.standard_create_file(self.folder_id_path)

##--------------------start-of-ensure_interface_files()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   def ensure_interface_files(self) -> None:

      """

      Ensures that the interface files are present and ready to be used.\n

      Parameters:\n
      self (object - fileEnsurer) : the fileEnsurer object.\n

      Returns:\n
      None.\n

      """

      util.standard_create_file(self.client_json_path)

      util.modified_create_file(self.last_run_path, "")