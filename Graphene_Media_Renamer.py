#!/usr/bin/python
import os, sys, re


# Picture formates - Lists
png_list = []
jpg_list = []
jpeg_list = []

# Video formates - Lists
mp4_list = []

# Audio formates - Lists
mp3_list = []
oog_list = []

# Acceptable input
reject = ['0', 'n', "no", 'false', 'disabled', 'disable', 'reject', 'deactivate', 'off']
accept = ['1', 'y', 'yes', 'ye', 'true', 'enable', 'enabled','activate','accept', 'on']

# Ensure valid working directory (contains any valid formates)
while 1:
    # Set working directory
    working_directory = input('Working directory? (paste full path) --> ')
    no_valid_files = False
    
    # If directory exists 
    if(os.path.exists(working_directory)):
        print('Directory exists, searching for formates...')

        # Searches for valid formates and puts them to lists

        # simplify
        for x in os.listdir(working_directory):
            if x.endswith(".png"):
                png_list.append(x)
            if x.endswith(".jpg"):
                jpg_list.append(x)
            if x.endswith(".jpeg"):
                jpeg_list.append(x)
            if x.endswith(".mp4"):
                mp4_list.append(x)
        
        # Sum the amount of valid file formates
        file_count = len(png_list) + len(jpg_list) + len(jpeg_list) + len(mp4_list) 
        
        # Breaks if more than 1 valid formate found
        if file_count >= 1: 
            print(file_count + " valid file formate found.")
            break

        # If no valid file formates found, try a different directory
        else: 
            no_valid_files = True

    ###  Unique error message  ###         
    # Not a valid directory
    if no_valid_files == False: 
        print("Working directory not found... Try a different directory.")
    
    # If no valid formates found in a valid directory
    if no_valid_files == True: 
        print('No valid file formates found in "' + working_directory + '" ... Try a different directory maybe?')
    

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
#
# (copy over files before? Or create COPY to create? )
# because the script takes the original file, renames it and moves it (i.e., no backup).

def media_search(media,):  
    for files in media:   # Cycle through IMAGE files. 
            # Split filename
            file_name = re.split("[_.-]" , files)
            date_index = file_name[1]
            time_index = file_name[2]
            file_extension = file_name[3]

            if debugging == True:
                print("String split: " + file_name)
                print("Date index : " + date_index)
                print("Time index : " + time_index)
                print("File extension : " + file_extension)
                print("")
            
            date_formate = date_index[0:4] + "." + date_index[4:6] + "." + date_index[6:8]
            time_formate = time_index[0:2]  + "." + time_index[2:4] + "." + time_index[4:6]
            new_date_formate = date_formate + "_" + time_formate + "--" + "P4a" + file_extension 
            
            if debugging == True: 
                print("New date formate : " + date_formate)
                print("New time formate : " + time_formate)
                print("New file formate : " + new_date_formate)
                print("")

            source = working_directory + "/" + files
            target = working_directory + "/" + target_dir + "/" + new_date_formate
            
            if debugging == True:
                print("")
                print("Original file at path: " + source)
                print("Renamed file at path: " + target)
                print("")   
            if debugging == True:
                print("")
                print("Original filename: " + str(files))
                print("File will be renamed to: " + new_date_formate)
                print ("")

            # rename
            os.rename(source, target)
            if debugging == True:
                print('File renamed.')
