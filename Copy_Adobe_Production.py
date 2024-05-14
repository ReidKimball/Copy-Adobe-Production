import os
import shutil
import sys

DEBUG_MODE = False

def copy_and_rename_production(source_path, new_name):    
    # Ensure the provided path exists, if not then raise error
    if not os.path.exists(source_path):
        raise ValueError(f"Source folder '{source_path}' not found.")    

    # Now build the new path
    # Extract the root folder path from the source path
    root_folder_path = os.path.dirname(source_path) # returns the parent folder of the path the user gave
    print(f"\nRoot folder is {root_folder_path}")

    # Generate the target folder path using the root + new name
    target_path = os.path.join(root_folder_path, new_name)
    print(f"\nTarget path is {target_path}")

    # Check if the target folder does not exist
    if not os.path.exists(target_path):
        # Copy the contents of the source folder
        try:
            if DEBUG_MODE:
                print(f"\nCopying production folder source: {source_path} contents to: {target_path}")
            shutil.copytree(source_path, target_path)
            print(f"\nCopied production folder contents to: {target_path}")
        except shutil.Error as e:
            raise OSError(f"Failed to copy production folder contents: {e}") from e
    else:
        sys.exit(f"\nTarget folder '{target_path}' already exists. Cannot continue.\n")

    # oiriginal source .prodset file to be renamed
    prodset_filename = os.path.basename(source_path) + ".prodset"
    if DEBUG_MODE:
        print(f"\nFile to be renamed: {prodset_filename}")

    target_prodset_path = os.path.join(target_path, prodset_filename) # full path and file name of the original source file
    new_target_prodset_path = os.path.join(target_path, f"{new_name}.prodset") # full path and file name of the new .prodset file
    if DEBUG_MODE:
        print(f"\ntarget_prodset_path is: {target_prodset_path}")
        print(f"\nnew_target_prodset_path is: {new_target_prodset_path}")

    if os.path.exists(target_prodset_path): # Check if target file exists in the new folder
        try:
            if DEBUG_MODE:
                print(f"\nRenaming file from {target_prodset_path} to {new_target_prodset_path}") 
            os.rename(target_prodset_path, new_target_prodset_path) # two arguments 1) target file 2) new file, then rename target file with new name
            print(f"\nRenamed .prodset file to: {new_name}.prodset") # assuming we get there, then exit function and go to line 91
        except OSError as e: # errors such as modify permissions not allowed
            raise OSError(f"Failed to rename .prodset file: {e}") from e
    else: # the target file does not exist in the new folder, so there's nothing to rename
        print(f"\nOriginal .prodset file not found in {source_path}. Adobe Premiere Pro may not open the project correctly.")

def main():
    __version__ = "0.0.2-pre1" # adopted convention to store version info as "major.minor.patch" or major.minor.patch-prerelease"
    
    """
    Interactive prompt to guide the user through the process.
    """
    if os.name == 'nt':
        os.system('cls') # clears the screen in terminal window
        print("Running on Windows")
        
    elif os.name == 'posix':
        os.system('clear') # clears the screen in terminal window
        print("Running on Unix-based system (e.g., Linux, macOS)")
    else:
        print("Running on an unknown operating system")

    # print welcome info for user
    print(f"Welcome to the Copy Adobe Production Uility v{__version__}"
          "\nThis will copy an existing Production folder and rename it for a new Production. "
          "\nStart by entering the full path to the source Production folder. "
          "\nEX: C:\Film Projects\JUMPCUT Productions "
          "\nBe sure to leave out the end slash.")
    
    # store the path the user enters into a string variable named source_path
    # input is a function that allows the user to input text and stores it as a string
    source_path = input("Which Adobe Premiere Pro Production folder do you want copied? Enter the full path without final slash: ")
    print(f"\nCopying {source_path}") # f-strings allow you to embed variables to be printed within quotation marks instead of "text" + variable + "more txt"

    # do this again but now the name of the Production, which will be the name of the new folder we'll make
    new_name = input("\nWhat is the new name for your Production? ")
    print(f"\nNew folder name: {new_name}")

    try:
        copy_and_rename_production(source_path, new_name)
        print("\nProduction copied and renamed successfully!\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__": # __name__ is a special variable that is set to main if this script is run directly rather than as a module.
    main() # run the main function above.
