# INTRODUCTION
# This file_renamer.py utility can be used to remove the 3 digit and space that appear at the begging of rom titles
# This file_renamer.py utility can be used to remove a single space that appears at the begging of rom titles

# INSTRUCTIONS
# Place this file in the specific ROM directory for the rom collection you want to fix (i.e. "/Roms/GBA")
# In the terminal/cmd, navigate to the same directory you placed this file (i.e. "cd /roms/GBA")
# Run the file from within the directory using "pyhton3 file_renamer.py"

# EXPECTED RESULTS
# You should see a print out of each file the process is renaming, and skipping the ones it does not


from curses.ascii import isdigit
import os

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
        new_name = ""

        ## USE THIS IF YOU NEED TO REMOVE 3 DIGITS AND SINGLE SPACE FROM BEGINNING OF ROM TITLE
        if name[0].isdigit() and name[1].isdigit() and name[2].isdigit():
            print("")
            print(f"Old Name: {name}")
            print("converting name")
            new_name = name[4:]
            try:
                os.rename(name, new_name)
            except:
                print(f"something went wrong trying to rename {name}")
            print(f"new name: {new_name}")
        else:
            print("name skipped")
        name = new_name
        print("")

        ## USE THIS IF YOU NEED TO REMOVE A SINGLE SPACE FROM BEGINNING OF ROM TITLE
        # if name[0] == " ":
        #     new_name = name[1:]
        #     try:
        #         os.rename(name, new_name)
        #     except:
        #         print(f"something went wrong trying to rename {name}")
        #     print(f"new name: {new_name}")
        # else:
        #     print("name skipped")
        # name = new_name
        # print("")
    # for name in dirs:
    #     print(os.path.join(root, name))
