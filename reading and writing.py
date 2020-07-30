#import os
#if you have the strings of a filepath, you can turn them into a filepath using os.path.join('string1', 'string2', 'string3'
#e.g. os.path.join ('documents', 'coding', 'python') returns documents\\coding\\python (two \ so it recognises the \ as a \)
#you can also do shit like this
#names = ["cat", "dog", "sheep"]
#for filename in names:
#   print(os.join.filename)

#you can get the current working directory of a file with os.getcwd()
#you can change the cwd with os.chdir('directorypath') but this will display an error if you try change to a directory that doesn't exist

#an absolute path always starts from the root folder and thus the filepath always starts with C:\
#a relative path uses things like .(meaning this folder) and ..(meaning parent folder, or "go one folder back")

#Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
#Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
#Calling os.path.relpath(path, start) will return a string of a relative path #from the start path to path. If start is not provided, the current working #directory is used as the start path

#everything before the final slashes is the dir name, and the last bit is the base name
#if path = 'C:\\Windows\\System32\\calc.exe', os.path.bassname(path) would be calc.exe, os.path.dirname(path) would be C:\\Windows\\System32
#os.path.split() would return both in a tuple

#os.path.getsize([path]) returns the size in bites of that file
#os.listdir([path]) will list all of the files in that path

#Calling os.path.exists(path) will return True if the file or folder referred to in the argument exists and will return False if it does not exist.
#Calling os.path.isfile(path) will return True if the path argument exists and is a file and will return False otherwise.
#Calling os.path.isdir(path) will return True if the path argument exists and is a folder and will return False otherwise.

#use .open(absolute/relative file path) to open a file
#you can use .read() to have the files contents printed as a string
#.readlines() will return a list of each string
#if you pass 'w' as the second argument in .open(), the document will be in write mode, allowing you to write over it. Doing this essentially starts the file form scratch, be warned
#passing 'a' as the second argument opens the file in append mode, allowing you to add text to the end
#once your done use .close()

