import os
import datetime

def run_command(command): #define a function
    return os.system(command)

def show_datetime():
    return datetime.datetime.today() 

#run_command("df -h")  #calling function
#run_command("uptime") #calling function
#run_command("time") #calling function
today=show_datetime() #if you are returning , catch the function
print(today)