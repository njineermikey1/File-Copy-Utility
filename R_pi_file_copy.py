'''
    This is a program to automate copying files from the host to
    the raspberry pi connected via ssh. It features a file selection
    dialog and user for hostname,, password and destination path.
    Copies multiple files. Use /home/... for path structure.
'''

import tkinter as tk
import tkinter.filedialog as filedialog
import paramiko
import os

# Set up the SSH client
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Set up the UI
root = tk.Tk()
root.withdraw()

# Get the remote machine details - remove docstring and delete hardcoded info for release.
'''
hostname = input("Enter the remote machine hostname: ")
username = input("Enter the remote machine username: ")
password = input("Enter the remote machine password: ")
'''

hostname = 'eisbpi2'    # Delete before release
username = 'mainuser'   # Delete before release
password = '101i10tw'   # Delete before release

# Connect to the remote machine over SSH
ssh.connect(hostname, username=username, password=password)

# Set up the SFTP client
sftp = ssh.open_sftp()

# Get the local files to copy
filepaths = filedialog.askopenfilenames()

# Get the remote directory to copy to. For the pi, use /home/<username>/<Directory>/<Directory>/...
# Path is case-sensitive
# Delete hardcoded path for production release

# remotedir = input("Enter the remote directory to copy to: ")

remotedir = '/home/mainuser/Transfer'

# Copy the files to the remote directory
for filepath in filepaths:
    # Get the file name and extension
    filename = os.path.basename(filepath)
    # Copy the file to the remote directory
    sftp.put(filepath, remotedir + "/" + filename)

# Close the SFTP and SSH clients
sftp.close()
ssh.close()