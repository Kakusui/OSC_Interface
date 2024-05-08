# OSC Interface

## Overview
The OSC Interface is an open-source tool designed to automate the retrieval of files from Google Drive and distribute them into predetermined locations. This software simplifies managing and organizing files, offering integration with their Google Drive accounts.

## To Use
Provided you're actually serious about using this software, please email [contact@kakusui.org](mailto:contact@kakusui.org) to request a client_secrets.json file.

Simply download the source code, set up your localconfig directory by creating the directory and adding the following files:
- downloaded_files_directory_name (name of the directory to download files to, this will be newly created locally and also be where your files are transferred to)
- file_paths_to_transfer.txt (Additional file paths to transfer to the target location, these should be full local paths, one per line)
- google_folder_ids.txt (the folder ids of the folders you want to download from, these can be found in the URL of the folder)
- google_folder_names.txt (the names of the folders you want to download from, these should be the names of the folders in your Google Drive)
- target_location.txt (where to put the files, this should be a full local path, or a usb stick like E://)

Once this is completed, you can simply run the run.py file and log in through Google, and your transfer will complete.

## Privacy and Data Usage
By using the OSC Interface, you agree to the Privacy Policy, which outlines the following:
- OSC Interface can modify, delete, and view any files in your Google Drive that you have specified in the application's configuration.
- Users give consent for these actions by linking their Google Drive with OSC Interface.
- The privacy policy may be updated at any time; users are encouraged to review it periodically.

## Open Source Licensing
The OSC Interface is distributed under the GNU General Public License version 3 (GPLv3), promoting open-source principles:
- **Freedom to Use:** You can use the software for any purpose.
- **Freedom to Modify:** You can modify the software according to your needs.
- **Freedom to Share:** You can redistribute the software and your modifications under the same license.

Please refer to the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.html) for a detailed understanding of your rights and obligations.

## Terms of Service
By using OSC Interface, you are agreeing to our Terms of Service, which include:
- **Eligibility:** Users must be old enough to have a Google account to use OSC Interface.
- **Prohibited Activities:** Users are prohibited from using the software in any way that interferes with its normal operation or with any other user's use and enjoyment of the software.
- **Modifications to the Software:** Users may modify the source code of OSC Interface as long as any modifications or derivative works are distributed under the same GPL license.
- **Intellectual Property:** No trademarks or proprietary rights are claimed in the project beyond those covered by the GPLv3 license.
- **Disclaimer of Warranties:** The software is provided "as is," without warranties of any kind.
- **Changes to Terms:** Terms may be modified at any time, with or without notice.

## Intellectual Property
No trademarks or proprietary rights are claimed in the project beyond those covered by the GPLv3 license.

## Support
For questions or support, please contact [contact@kakusui.org](mailto:contact@kakusui.org).

---
