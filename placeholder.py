#!/usr/bin/python
import os, sys, re


# All valid files
media_list = []

# Picture formates - Lists
png_list = []
jpg_list = []
jpeg_list = []

# Video formates - Lists
mp4_list = []
mov_list  = []


# Audio formates - Lists
mp3_list = []
ogg_list = []
m4a_list = []

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
        for x in os.listdir(working_directory):
            if x.endswith(".png"):
                png_list.append(x)
            if x.endswith(".jpg"):
                jpg_list.append(x)
            if x.endswith(".jpeg"):
                picture_list.append(x)
            if x.endswith(".mp4"):
                video_list.append(x)
        
        # Sum the amount of valid file formates
        media_list = len(png_list) + len(jpg_list) + len(picture_list) + len(video_list) 
        
        # Breaks if more than 1 valid formate found
        if media_list >= 1: 
            print(media_list + " valid file formate found.")
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
    debugging = input("Enable debugging? (y/n)   ").lower()
    if debugging in accept:  
        print('Debugging enabled.')
        break
    if debugging in reject:
        print('Debugging disabled.')
        break
    print('Invalid input. Please try again. ("y" or "n")')


#  Might not need this? 
while 1: 
    interactive = input("Enable interactive mode? (y/n)   ").lower()
    if interactive == "y":
        print('Interactive mode enabled.')
        break
    if interactive == "n":
        print('Interactive mode disabled.')
        break
    print('Invalid input. Please try again. ("y" or "n")')

media_list = []
media_list_img = []
media_list_vid = []


target_dir = "_rename"
target_path = working_directory + "/" + target_dir

def media_search(media_split):
    media_search_list=[]
    
    for files in media_list:
        if media_split.upper() in files.upper():    #os.path.isfile(os.path.join(working_directory, files) & a.upper == "img"): #Totale images in path 
            media_search_list.append(files)

        print("There are " + str(len(media_search_list)) + "files containint " + media_split + " formate.")

    for files in media_search_list: # Cycle through IMAGE files. 
        if () in media_search_list.upper():

            file_index = re.split("[_.-]" , files)[1]  # Split based on standard formate 
            if file_index.isnumeric():
                year_split = file_index[0:4]
                month_split = file_index[4:6]
                day_split = file_index[6:8]
                date_formate = year_split + "." + month_split + "." + day_split
                print("Date value for this file is: " + date_formate)
            else: 
                #if interactive == 'y':
                    #
                if interactive == 'n':
                    year_split = "YYYY"
                    month_split = "MM"
                    day_split = "DD"
                    date_formate = year_split + "." + month_split + "." + day_split + "+" + file_index + "+"
                    print("String split returned with: " + file_index)
                    print("Invalid formate or date not found. Using unknown date formate: " + date_formate)

            #Time splitting  ---  Checks whether there is time information by excluding alphabetic input (ifnot set to unknown time)
            time_index = re.split("[_.-]" , files)[2]  # Split based on standard formate
            if time_index.isnumeric():
                hour_split = time_index[0:2] 
                min_split = time_index[2:4]
                sec_split = time_index[4:6]
                time_formate = hour_split + "." + min_split + "." + sec_split
                print("Time value for this file is: " + time_formate)
            else: 
                #if interactive == 'y':
                    #
                #if interactive == 'n':
                hour_split = "HH"
                min_split = "MM"
                sec_split = "SS"
                time_formate = hour_split + "." + min_split + "." + sec_split + "+" + time_index + "+"
                print("String split returned with: " + time_index)
                print("Invalid formate or time not found. Using unknown time formate: " + time_formate)
            
            #File extension
            file_extension = "." + re.split("[_.-]" , files)[3]
            print("The file extension for this file is: " + str(file_extension))

            #Rename shorthand
            new_date_formate = date_formate + "_" + time_formate + "--" + "P4a" + file_extension 
            source_file = working_directory + "/" + files
            target = working_directory + "/" + target_dir + "/" + new_date_formate
            
            if debugging == True:
                print("")
                print("Original file at path: " + source_file)
                print("Renamed file at path: " + target)
                print("")   
            if debugging == True:
                print("")
                print("Original filename: " + str(files))
                print("File will be renamed to: " + new_date_formate)
                print ("")

            if interactive == "y":    
                while True:
                    accept_img_change = input('Do you accept these changes? (y/n)')
                    if accept_img_change == "y":
                        print("Renaming...")
                        break
                    if accept_img_change == "n": 
                        print("Not renaming file...")
                        break
                    print('Invalid input. Please try again. ("y" or "n")')
            if interactive == 'n':
                accept_img_change = 'y' 
            if accept_img_change =="y": 
                os.rename(source_file, target)
                print('File renamed.')