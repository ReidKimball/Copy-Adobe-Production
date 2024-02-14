import os
import shutil

def copy_and_rename_production(source_path, new_name):
    """
    Copies a template Production folder and renames it and its .prodset file.

    Args:
        source_path (str): Path to the source Production folder.
        new_name (str): New name for the copied Production.

    Raises:
        ValueError: If the source folder or .prodset file is not found.
        OSError: If an error occurs during copying or renaming.
    """
    
    # Ensure the provided paths are valid
    if not os.path.exists(source_path):
        raise ValueError(f"Source folder '{source_path}' not found.")

    # Extract the root folder path from the source path
    root_folder_path = os.path.dirname(source_path)
    print(f"Root folder is {root_folder_path}")

    # Generate the target folder path using the root and new name
    target_path = os.path.join(root_folder_path, new_name)
    print(f"Target path is {target_path}")


    # Check if the target folder already exists and handle accordingly
    if os.path.exists(target_path):
        print(f"Target folder '{target_path}' already exists. Skipping folder creation.")
    else:
        # Create the new Production folder in the root folder
        try:
            # os.makedirs(target_path) this might not be needed.
            print(f"Created new Production folder: {target_path}")
        except OSError as e:
            raise OSError(f"Failed to create production folder: {e}") from e


    # Copy the contents of the source folder
    try:
        print(f"Copying production folder source: {source_path} contents to: {target_path}")
        shutil.copytree(source_path, target_path, symlinks=True)
        print(f"Copied production folder contents to: {target_path}")
    except shutil.Error as e:
        raise OSError(f"Failed to copy production folder contents: {e}") from e

    # Rename the .prodset file
    prodset_filename = os.path.basename(source_path) + ".prodset"
    print(f"File to be renamed: {prodset_filename}") # needs to be JCRT_EPXXX.prodset

    #source_prodset_path = os.path.join(source_path, prodset_filename) # this is needed to rename the source file
    #print(f"source_prodset_path is: {source_prodset_path}")

    target_prodset_path = os.path.join(target_path, prodset_filename) # this is needed to rename the source file
    new_target_prodset_path = os.path.join(target_path, f"{new_name}.prodset") # this needs to be the new path and file
    print(f"target_prodset_path is: {target_prodset_path}")
    print(f"new_target_prodset_path is: {new_target_prodset_path}")

    if os.path.exists(target_prodset_path): # Check if target file exists in the new folder
        try:
            print(f"Renaming file from {target_prodset_path} to {new_target_prodset_path}") 
            # os.rename(source_prodset_path, target_prodset_path)
            os.rename(target_prodset_path, new_target_prodset_path) # Rename target file with new name
            # print(f"Renamed .prodset file to: {target_prodset_path}")
            print(f"Renamed .prodset file to: {new_name}.prodset")
        except OSError as e:
            raise OSError(f"Failed to rename .prodset file: {e}") from e
    else:
        print(f".prodset file not found in {source_path}. Adobe Premiere Pro may not open the project correctly.")


def main():
    __version__ = "0.0.1-pre1"
    
    """
    Interactive prompt to guide the user through the process.
    """

    os.system('cls')
    # on Windows use 'cls' instead of 'clear'

    print(f"Welcome to the Copy Adobe Production Uility v{__version__}"
          "\nThis will copy an existing Production folder and rename it for a new Production. "
          "\nStart by entering the full path to the source Production folder. "
          "\nEX: C:\Film Projects\JUMPCUT Productions "
          "\nBe sure to leave out the end slash.")
    source_path = input("Which Adobe Premiere Pro Production folder do you want copied? Enter the full path without final slash: ")
    print(f"Copying {source_path}")

    new_name = input("What is the new name for your Production? ")
    print(f"New folder name: {new_name}")
    try:
        copy_and_rename_production(source_path, new_name)
        print("Production copied and renamed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
