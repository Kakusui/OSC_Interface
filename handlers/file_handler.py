## built-in libraries
import os
import typing
import logging

class FileHandler():

    """
    
    The FileHandler class contains methods for handling files.

    """

##--------------------start-of-standard_create_directory()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def standard_create_directory(directory_path:str) -> None:

        """

        Creates a directory if it doesn't exist, as well as logs what was created.

        Parameters:
        directory_path (str) : path to the directory to be created.

        """

        if(os.path.isdir(directory_path) == False):
            os.mkdir(directory_path)
            logging.info(directory_path + " was created due to lack of the folder.")

##--------------------start-of-modified_create_directory()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def modified_create_directory(directory_path:str, path_to_check:str) -> None:

        """

        Creates a directory if it doesn't exist or if the path provided is blank or empty, as well as logs what was created.

        Parameters:
        directory_path (str) : path to the directory to be created.
        path_to_check (str) : path to check if it is blank.

        """

        if(os.path.isdir(directory_path) == False or os.path.getsize(path_to_check) == 0 or os.path.exists(path_to_check) == False):
            os.mkdir(directory_path)

            reason = f"was created due to lack of {directory_path}." if os.path.isdir(directory_path) == False else f"was created due to {path_to_check} being blank or empty."

            logging.info(directory_path + " " + reason)

##--------------------start-of-standard_create_file()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def standard_create_file(file_path:str) -> None:

        """

        Creates a file if it doesn't exist, truncates it, as well as logs what was created.

        Parameters:
        file_path (str) : path to the file to be created.

        """

        if(os.path.exists(file_path) == False):
            logging.info(file_path + " was created due to lack of the file.")
            with open(file_path, "w+", encoding="utf-8") as file:
                file.truncate()

##--------------------start-of-modified_create_file()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def modified_create_file(file_path:str, content_to_write:str, omit:bool=True) -> bool:

        """

        Creates a path if it doesn't exist or if it is blank or empty, writes to it, as well as logs what was created and written.

        Parameters:
        file_path (str) : path to the file to be created.
        content to write (str) : content to be written to the file.
        omit (bool | optional | default = True) : whether to omit the content written to the file in the log.

        Returns:
        did_overwrite (bool) : whether the file was created.

        """

        did_overwrite = False

        if(os.path.exists(file_path) == False or os.path.getsize(file_path) == 0):
            logging.info(file_path + " was created due to lack of the file or because it is blank.")
            with open(file_path, "w+", encoding="utf-8") as file:
                file.write(content_to_write)

                if(omit):
                    content_to_write = "(Content was omitted.)"
                logging.info(file_path + " was created and written to with the following content: " + content_to_write)

            did_overwrite = True

        return did_overwrite
    
##--------------------start-of-standard_overwrite_file()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def standard_overwrite_file(file_path:str, content_to_write:typing.Union[str, typing.List[str]], omit:bool = True) -> None:

        """

        Writes to a file, creates it if it doesn't exist, overwrites it if it does, as well as logs what was written.

        Parameters:
        file_path (str) : path to the file to be overwritten.
        content to write (str | list - str) : content to be written to the file.
        omit (bool | optional | default = True) : whether to omit the content written to the file in the log.

        """

        if(isinstance(content_to_write, list)):
            content_to_write = "\n".join(content_to_write)

        with open(file_path, "w+", encoding="utf-8") as file:
            file.write(content_to_write)

        if(omit):
            content_to_write = "(Content was omitted.)"
        
        logging.info(file_path + " was overwritten with the following content: " + content_to_write)

##--------------------start-of-clear_file()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def clear_file(file_path:str) -> None:

        """

        Clears a file, as well as logs what was cleared.

        Parameters:
        file_path (str) : path to the file to be cleared.

        """

        with open(file_path, "w+", encoding="utf-8") as file:
            file.truncate()

        logging.info(file_path + " was cleared.")
        
##--------------------start-of-standard_read_file()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def standard_read_file(file_path:str) -> str:

        """

        Reads a file and returns its content.

        Parameters:
        file_path (str) : path to the file to be read.

        Returns:
        content (str) : the content of the file.

        """

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content