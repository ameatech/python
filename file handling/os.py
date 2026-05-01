import os
#print(os.getcwd()) #get current working directory
path=os.chdir(r"c:\python\isr\lab") #change directory
#print(os.listdir()) #list files in current directory
#print(os.getcwd())
#
#print(os.walk(os.getcwd()))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("current path:", dirpath)
    print("directories", dirnames)
    print("files", filenames)
    print()
