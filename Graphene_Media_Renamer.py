#!/usr/bin/python
from doctest import testfile
from logging import root
import os, sys, re
from tkinter import N

###   Temp   ### 
renamer = False # Toggles:
def hold(): # Hold 
    while 1:
        hold_input = input("Exit script?  -->  ")
        if str(accept) in hold_input:
            print("exiting script...")
            sys.exit()
        if str(reject) in hold_input:
            print("continuing...")
            break
        else:
            print("Invalid input.")
###   Temp  ###

# Formates: 
file_list = [] # All valid formates
picture_list = [] # Pictures
video_list = [] # Videos
screenrecording_list = [] # Screenrecordings 

# Acceptable input
reject = ['0', 'n', "no", 'false', 'disabled', 'disable', 'reject', 'deactivate', 'off']
accept = ['1', 'y', 'yes', 'ye', 'true', 'enable', 'enabled','activate','accept', 'on']

# Ensure valid working directory (contains any valid formates)
while 1:
    working_directory = "D:\.OnHold\.Sync_T_Sch"
    # working_directory = input('Working directory? (paste full path) --> ')
    no_valid_files = False
    
    # If directory exists 
    if(os.path.exists(working_directory)):
        print('Directory exists, searching for formates...')

        # Searches for valid formates and puts them to lists
        for x in os.listdir(working_directory):
            if x.endswith(".jpeg"):
                picture_list.append(x)
                file_list.append(x)
            if x.endswith(".mp4"):
                video_list.append(x)
                file_list.append(x)
            if "screen" in x: # Because same extension as .mp4
                screenrecording_list.append(x)
                file_list.append(x)
            
        # Breaks if more than 1 valid formate found
        if len(file_list) >= 1: 
            print(str(len(file_list)) + " valid file formate found.")
            print("There are '" + str(len(picture_list)) + "' pictures in this directory.")
            print("There are '" + str(len(video_list)) + "' videos in this directory.")
            print("There are '" + str(len(screenrecording_list)) + "' screenrecordings in this directory.")
            break

        # If no valid file formates found, try a different directory
        if file_list <= 0: 
            no_valid_files = True

    ###  Unique error message  ###         
    # Not a valid directory
    if no_valid_files == False: 
        print("Working directory not found... Try a different directory.")
    
    # If no valid formates found in a valid directory
    if no_valid_files == True: 
        print('No valid file formates found in "' + working_directory + '" ... Try a different folder maybe?')
    
# Debugging//Extra information?
while 1:
    debugging = input("Enable debugging? (y/n) --> ").lower()
    if debugging in accept:  
        print('Debugging enabled.')
        break
    if debugging in reject:
        print('Debugging disabled.')
        break
    print('Invalid input. Please try again. ("y" or "n")')

target_path = working_directory + "/_rename"

# Create new folder for renamed files  

if not(os.path.exists(target_path)):
    print("Rename folder  not found. Creating rename folder.")
    os.mkdir(target_path)
    print("Rename folder created at: " + target_path + ".")
if (os.path.exists(target_path)):
    print("Rename folder created.")

hold()

#
# (copy over files before? Or create COPY to create? )
# because the script takes the original file, renames it and moves it (i.e., no backup).

for files in file_list:   # Cycle through all lists (?) 
        file_and_extension = os.path.splitext(files)   # Thing that split by "name" and "extension" -- doesn't really matter, but cool 
        file_name = re.split("[_.-]" , file_and_extension[0])
        date_index = file_name[1]
        time_index = file_name[2]

        if debugging == True:
            print("String split: " + file_name)
            print("Date index : " + date_index)
            print("Time index : " + time_index)
            print("File extension : " + file_and_extension[1])
            print("")
        
        date_formate = date_index[0:4] + "." + date_index[4:6] + "." + date_index[6:8] #date formate
        time_formate = time_index[0:2]  + "." + time_index[2:4] + "." + time_index[4:6]
        new_date_formate = date_formate + "_" + time_formate + "--" + "P4a" + file_and_extension[1] 
        
        if debugging == True: 
            print("New date formate : " + date_formate)
            print("New time formate : " + time_formate)
            print("New file formate : " + new_date_formate)
            print("")
        if debugging == True:
            print("Original filename: " + str(files))
            print("File will be renamed to: " + new_date_formate)
            print ("")

        source = working_directory + "/" + files
        target = target_path + "/" + new_date_formate
        
        if debugging == True:
            print("Original file at path: " + source)
            print("Renamed file at path: " + target)
            print("")   

        # Renamer
        if renamer == True:
            os.rename(source, target)
            if debugging == True:
                print('File renamed.')
        if renamer == False:
            print("End of the line...")


