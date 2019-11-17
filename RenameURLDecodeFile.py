import os
import urllib.parse

# Insert the directory where you would like to find and rename your files
path = "/your_path"

# The var onlyfiles gets all file names from path in a array
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
# If you want see all files names, uncomment the next line:
    #print(*onlyfiles, sep='\n')

i = 0

# Insert the var path to os.chdir to know where will rename
os.chdir(path)

# For to rename all files in var onlyfiles
for file in onlyfiles:
    rename(file, urllib.parse.unquote_plus(file))
    i += 1
    print("File " + str(i) + " converted")


