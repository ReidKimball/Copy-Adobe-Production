# Copy Adobe Production Utility

This utility allows you to copy an existing Adobe Premiere Pro Production folder and rename it for a new production.

## PC/Mac Compatibility
This has only been tested on Windows 11. I could use help having a few people test it on Mac OS and report back how well it works.

## Installation
Install Python on your local machine. https://www.python.org/downloads/
Download the Copy Adobe Production.py and save it where you save other video editing tools you use.

## Usage
Launch the Copy_Adobe_Production.py script. This can be done by double clicking the file in Windows Explorer, or opening a terminal (Start > Windows PowerShell) and typing “python Copy_Adobe Production.py”.

When prompted, enter the full path to the existing Production folder you want to copy. For example: 

<code>C:\Film Projects\Production EP01</code>

Note: Do not include the final slash in the path.

Enter a name for the new Production folder. This will be used to rename the copied folder and associated .prodset file. For example:

<code>Production EP02</code>

The utility will copy the Production folder to the same parent folder, rename it based on your input, and rename the associated .prodset file.
Once complete, you will have a duplicate Production folder ready fo your new project!

Let me know if you need any clarification or have additional questions on using the utility.

## Notes:
The terminal window will display many printed messages. These are useful for understanding what the program is doing under the hood. They will be removed when the tool is more refined and bugs are reduced.

## Bugs:
* Does not check for valid path before asking for new production folder name
* Tries to copy production folder even though it previously said folder already exists
* Doesn’t gracefully exit if Production folder already exists

# Use of AI
Generative AI was used to assist in the writing of this code.