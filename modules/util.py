## built in modules
import os
import time

##--------------------start-of-standard_create_directory()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def standard_create_directory(directory_path:str):

    """

    Creates a directory if it doesn't exist, as well as prints to console what was created, along with a slight delay.\n

    Parameters:\n
    directory_path (str) : path to the directory to be created.\n

    Returns:\n
    None.\n

    """

    if(os.path.isdir(directory_path) == False):
        os.mkdir(directory_path)
        print(directory_path + " created due to lack of the folder")
        time.sleep(0.1)

##--------------------start-of-standard_create_file()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def standard_create_file(file_path:str):

    """

    Creates a file if it doesn't exist, truncates it,  as well as prints to console what was created, along with a slight delay.\n

    Parameters:\n
    file_path (str) : path to the file to be created.\n

    Returns:\n
    None.\n

    """

    if(os.path.exists(file_path) == False):
        print(file_path + " was created due to lack of the file")
        with open(file_path, "w+", encoding="utf-8") as file:
            file.truncate()

##--------------------start-of-modified_create_file()------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def modified_create_file(file_path:str, content_to_write:str):

    """

    Creates a path if it doesn't exist or if it is blank or empty, writes to it,  as well as prints to console what was created, along with a slight delay.\n

    Parameters:\n
    file_path (str) : path to the file to be created.\n
    content to write (str) : content to be written to the file.\n

    Returns:\n
    None.\n

    """

    if(os.path.exists(file_path) == False or os.path.getsize(file_path) == 0):
        print(file_path + " was created due to lack of the file or because it is blank")
        with open(file_path, "w+", encoding="utf-8") as file:
            file.write(content_to_write)
            
##-------------------start-of-clear_console()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def clear_console() -> None:

    """

    clears the console.\n

    Parameters:\n
    None.\n

    Returns:\n
    None.\n

    """

    os.system('cls' if os.name == 'nt' else 'clear')

##-------------------start-of-pause_console()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pause_console(message:str="Press enter to continue . . .") -> None:

    """

    pauses the console.\n

    Parameters:\n
    message (str - optional) : the message that will be displayed when the console is paused.\n

    Returns:\n
    None\n

    """

    if(os.name == 'nt'):  ## Windows
        os.system('pause /P f{message}')
    else: ## Linux
        input(message)

