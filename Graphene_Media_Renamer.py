#!/usr/bin/python
from distutils.file_util import copy_file
import os, sys, re

# Acceptable input
reject = ["0", "n", "no", "nop", "nope", "false", "disable", "disabled", "reject", "deactivate", "off"]
accept = ["1", "y", "ye", "yep", "yeah", "true", "enable", "enabled", "accept", "activate", "yes", "on", "yeh", "yh"]

################
###   Temp   ### 


renamer = False # Toggles:


def hold(string): # Hold 
    while 1:
        print("")
        print(string)
        hold_input = input("--->  ").lower()
        if  hold_input in accept:
            print("Exiting script...")
            sys.exit()
        if hold_input in reject:
            print("Continuing...")
            break
        else:
            print("Invalid input.")
###   Temp  ###
###############

# Formates: 
media_list = [] # All valid formates
picture_list = [] # Pictures
video_list = [] # Videos
screenrecording_list = [] # Screen recordings 
audio_list = [] # Audio recordings

# Ensure valid working directory (contains any valid formates)
while 1:
    working_directory = input('Working directory? (paste full path) --> ')
    no_valid_files = False 
    
    # If directory exists 
    if(os.path.exists(working_directory)):
        print('Directory exists, searching for formates...')

        # Searches for valid formates and puts them to lists
        for x in os.listdir(working_directory):
            # Basic GrapheneOS media formate things
            if x.endswith(".jpg" or ".png"):
                picture_list.append(x)
                media_list.append(x)
            if x.endswith(".mp4"):
                video_list.append(x)
                media_list.append(x)
                
            # Additional program
            if x.endswith(".ogg"):
                audio_list.append(x)
                media_list.append(x)
            
        # Breaks if more than 1 valid formate found
        if len(media_list) >= 1: 
            print(str(len(media_list)) + " valid file formate in " + working_directory +".")
            print("There are '" + str(len(picture_list)) + "' pictures in this directory.")
            print("There are '" + str(len(video_list)) + "' videos in this directory.")
            print("There are '" + str(len(screenrecording_list)) + "' screenrecordings in this directory.")
            print("There are '" + str(len(audio_list)) + "' audio files in this directory.")
            break

        # If no valid file formates found, try a different directory
        if media_list <= 0: 
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
        print("Debugging enabled.")
        debugging = True
        break
    if debugging in reject:
        print("Debugging disabled.")
        debugging = False
        break
    print("Invalid input. Please try again. ('y' or 'n')")
    print("")

# Create a copy of the renamed file instead of purely renaming (and moving it)?
while 1:
    copying = input("Enable copying? (y/n) --> ").lower()
    if copying in accept:  
        print("Copying enabled.")
        copying = True
        break
    if copying in reject:
        print("Debugging disabled.")
        copying = False
        break
    print("Invalid input. Please try again. ('y' or 'n')")
    print("")

target_file_path = working_directory + "/_rename"

# Create new folder for renamed files if copy is enabled  
if copying == True:
    if not(os.path.exists(target_file_path)):
        print("Rename folder  not found. Creating rename folder.")
        os.mkdir(target_file_path)
        print("Rename folder created at: " + target_file_path + ".")
        print("")
    if os.path.exists(target_file_path):
        print("Rename already exists... Skipping.")
        print("")

for files in media_list:
    file_and_extension = os.path.splitext(files)   # Thing that split by "name" and "extension" -- doesn't really matter, but cool 
    file_name = re.split("[_.-]" , file_and_extension[0])
    date_index = file_name[1]
    time_index = file_name[2]

    if debugging == True:
        print("String split: " + str(file_name))
        print("Date index : " + date_index)
        print("Time index : " + time_index)
        print("File extension : " + file_and_extension[1])
        print("")

    # Reformate
    date_formate = date_index[0:4] + "." + date_index[4:6] + "." + date_index[6:8] #date formate
    time_formate = time_index[0:2]  + "." + time_index[2:4] + "." + time_index[4:6]
    new_date_formate = date_formate + "_" + time_formate + "--" + "P4a" + file_and_extension[1] 
    
    if debugging == True:
        print("New date formate: " + date_formate)
        print("New time formate: " + time_formate)
        print("New file formate: " + new_date_formate)
        print("")
        print("Original filename: " + str(files))
        print("File will be renamed to: " + new_date_formate)
        print ("")

    # File paths 
    source_file = working_directory + "/" + files
    target_file = target_file_path + "/" + new_date_formate

    if debugging == True:
        print("Original file at path: " + source_file)
        print("Renamed file at path: " + target_file)
        print("")   

    # If copying is enabled
    if copying == True:
        # New variables for copying file thing
        source_file_copy_function = target_file_path + "/" + files 
        target_file_copy_function = target_file_path + "/" + new_date_formate
        # Check whether file exists or not (in either original or reformated) 
        if not(os.path.exists(source_file_copy_function)) and not(os.path.exists(target_file)):
            copy_file(source_file, target_file_path) # Copy file
            if debugging == True:                    
                print(source_file + " >> MOVED TO --> " + target_file_path)
            if renamer == True: # Rename the copied file 
                os.rename(source_file_copy_function, target_file_copy_function)
                if debugging == True:
                    print("File renamed.")
            if renamer == False: 
                print("End of the line...")
        # Print statement if file exists in either form
        if os.path.exists(source_file_copy_function) or os.path.exists(target_file_copy_function):
            if os.path.exists(source_file_copy_function):
                print("File already exists in its original form, in '_renamed'")
                print("File as: " + source_file_copy_function)
            else: 
                print("File already exists in its renamed form, in '_renamed'")
                print("File as: " + target_file_copy_function)

    # If copying is NOT enabled
    if copying == False: # This moves and renames the "working_directory" files (better for storage)
        # By also moving the files to another directory, we filter out other files that do not meet the criteria
        if renamer == True:
            os.rename(source_file, target_file)
            if debugging == True:
                print("File renamed.")
        if renamer == False:
            print("End of the line...")


    # hold("Exit script?")
    