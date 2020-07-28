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
