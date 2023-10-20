## built-in libaries
import os
import typing

## custom modules
from modules.fileEnsurer import fileEnsurer

class pathHandler:

    """
    
    Assembles paths for backup/transfer of SCF.\n

    """

##--------------------start-of-__init__()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, inc_file_ensurer:fileEnsurer) -> None:

        """
        
        Initializes the pathHandler class.\n

        Parameters:\n
        file_ensurer (object - fileEnsurer): The fileEnsurer object.\n

        Returns:\n
        None.\n

        """

        self.file_ensurer = inc_file_ensurer

        ##----------------------------------------------------------------/

##--------------------start-of-setup()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def setup(self) -> None:

        """

        Sets up the pathHandler object.\n

        Parameters:\n
        self (object - pathHandler): The pathHandler object.\n

        Returns:\n
        None.\n

        """

        self.ids, self.names = self.get_folder_properties()

        self.dirs:typing.Dict[int,str] = {}
        self.iteration_dirs:typing.Dict[int,str] = {}
        self.iteration_paths:typing.Dict[int,str] = {}

        for i, name in enumerate(self.names):
            self.dirs[i+1] = os.path.join(self.file_ensurer.scf_actual_dir, name)
            self.iteration_dirs[i+1] = os.path.join(self.dirs[i+1], "Current Iteration")
            self.iteration_paths[i+1] = os.path.join(self.iteration_dirs[i+1], "iteration.txt")

##--------------------start-of-get_folder_properties()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_folder_properties(self) -> typing.Tuple[typing.List[str], typing.List[str]]:

        """

        Gets the folder properties from the local config files.\n

        Parameters:\n
        self (object - pathHandler): The pathHandler object.\n

        Returns:\n
        folder_ids (list - str): The folder ids.\n
        folder_names (list - str): The folder names.\n
        
        """

        with open(self.file_ensurer.folder_ids_path, "r") as file:
            folder_ids = [line.strip() for line in file.readlines()]

        with open(self.file_ensurer.folder_names_path, "r") as file:
            folder_names = [line.strip() for line in file.readlines()]


        return folder_ids, folder_names
        

        

        

