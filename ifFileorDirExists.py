import pathlib

path = pathlib.Path("/etc/hosts")

print(path.exists())

print(path.is_file())

print(path.is_dir())

if path.is_file() == True:
    print (path,"is a file")
elif path.is_dir() == True:
    print (path,"is a dir")   