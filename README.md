# File Copy Utility

Automates file transfer from a windows client to a Raspberry pi headless host.

To copy a file when connected via ssh to a headless raspberry pi:

* Input Raspberry pi local name
* Input Raspberry pi root username
* Input Raspberry pi root user password
* Select file(s) from the file manager popup
* input path to destination directory

All fields are case-sensitive. The path statement should be formatted as:

* /home/username/destination

Use / before home or the tranfer will fail. 