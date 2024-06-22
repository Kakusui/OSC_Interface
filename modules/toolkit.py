## Copyright 2024 Kakusui LLC (https://kakusui.org/Okisouchi) (https://github.com/Kakusui) (https://github.com/Kakusui/osc_interface)
## Use of this source code is governed by a GNU General Public License v3.0
## license that can be found in the LICENSE file.

## built-in modules
import os

class Toolkit():

    """
    
    The class for a bunch of utility functions used throughout OSCInterface.

    """
##-------------------start-of-clear_console()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def clear_console() -> None:

        """

        Clears the console.

        """

        os.system('cls' if os.name == 'nt' else 'clear')

##-------------------start-of-pause_console()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def pause_console(message:str="Press any key to continue...") -> None:

        """

        Pauses the console.

        Parameters:
        message (str | optional) : the message that will be displayed when the console is paused.

        """

        print(message)  ## Print the custom message
        
        if(os.name == 'nt'):  ## Windows

            import msvcrt
            
            msvcrt.getch() 

        else:  ## Linux

            import termios

            ## Save terminal settings
            old_settings = termios.tcgetattr(0)

            try:
                new_settings = termios.tcgetattr(0)
                new_settings[3] = new_settings[3] & ~termios.ICANON
                termios.tcsetattr(0, termios.TCSANOW, new_settings)
                os.read(0, 1)  ## Wait for any key press

            finally:

                termios.tcsetattr(0, termios.TCSANOW, old_settings)
