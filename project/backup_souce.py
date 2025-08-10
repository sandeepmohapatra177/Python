import shutil
import os
import datetime

def backup_file(source,destination): # created a function
    today = datetime.date.today() #to add date of back up to file name
    backup_file_name = os.path.join(destination,f"backup_{today}")  #f:formatted string: add variable in a string as {}
    shutil.make_archive(backup_file_name,'zip',source) #shutil file operation, zip
    
source = "A:\Devops\Python\project"
destination = "A:\Devops\Python\project"     # need folder for back up
backup_file(source,destination)