import sys
import os
from shutil import copy
from time import sleep

get_user = os.getlogin() #Gets PC or Mac Name
print(get_user) #Prints to make sure it is correct

#Inserts user name into root directory path (where the back-up is stored).
path_to_root_directory = "/Users//Desktop/BackUpTest/Test.rtf" 
path_to_root_directory = path_to_root_directory[:7] + get_user + path_to_root_directory[7:]

print(path_to_root_directory) #Prints to make sure it is correct

#Inserts user name into drop directory path (where the back-up is going to be stored).
path_to_db_directory = "/Users//Dropbox/BUT"
path_to_db_directory = path_to_db_directory[:7] + get_user + path_to_db_directory[7:]

print(path_to_db_directory) #Prints to make sure it is correct

#path = path_to_db_directory


#Checks if there is a folder in Dropbox to send back ups to.
#If there is no folder, creates one.
if not os.path.exists(path_to_db_directory):
    os.makedirs(path_to_db_directory)

#Checks for an updated file in the root back-up folder - if so, sends it to the dropbox folder.
while 1:
    copy(path_to_root_directory, path_to_db_directory, follow_symlinks=True)
    print ('done')
    sleep(30) #Defines the back-up interval in seconds. (60s = 1min - of course)

#So now you just need to make it so that this script runs all the time,
#and starts running when the user starts up the PC.
