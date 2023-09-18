#importing module subprocess for allowing bash commands
#importing os module to interact with OS for various tasks
import subprocess
import os

#get username of this linux system using os module
get_username=os.getlogin()
#defining the directory & its path(for txt file we need) inside a variable to be used later in file handling
store_directory_path = f"/home/{get_username}/Details"
#defining the path with respect to the directory & file
file_path = os.path.join(store_directory_path, "Summary.txt")

#creating a directory named "Details" if it doesnot exists
if not os.path.exists(store_directory_path):
    os.makedirs(store_directory_path)

#bash commands for system information using lscpu and storing
# them into commands lists
command = ["lscpu | grep 'Byte Order'",
           "lscpu | grep 'Core(s) per socket'",
           "lscpu | grep 'Socket(s)'",
           "lscpu | grep 'Model name'",
           "lscpu | grep 'MHz'",
           "lscpu | grep 'Virtualization'",
           "lscpu | grep 'L1d cache' && lscpu |  grep 'L1i cache'",
           "lscpu | grep 'L2 cache'",
           "lscpu | grep 'L3 cache'",
           "free -h | awk '/Mem/ {print \"RAM Memory:                          \" $2}'"
           ]

#Opening and writing the generated results into Summary.txt' file
with open(file_path, "w") as file_path:
    for command in command:
        #executing each of the commands and storing inside 'result' var
        result = subprocess.check_output(command, shell=True, text=True)
        #printing the reuslts on console
        print(result)
        #writing the 'result' into the file path /home/{username}/Details/Summary.txt
        file_path.write(result)
        
#printing the completion message        
print(f"Summary.txt file created at: {store_directory_path}")