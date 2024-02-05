import os

#x = os.system("pwd")

# os.chdir("/home/vboxuser") #chnage directory

# #x = os.system("pwd")
# #to get cuurent working directory
# os.getcwd() 


# to print list of files in mentioned directory
# for i in os.listdir("/home/vboxuser/python"):
#     print(i)

#os.mkdir("/home/vboxuser/python/test") # to create directory

#os.mknod("/home/vboxuser/python/test/filecreatedbypython.txt")   #to crete file

#os.system("ls /home/vboxuser/python/test")

#os.makedirs("/home/vboxuser/python/sub1/sub2")#to create directory and sub directory sametime

#get os environment values
# for i in os.environ:
#     print(i)

# get value of specific Environment var
# x=os.environ.get("PATH")   
# print(x)

# userid=os.getuid()
# grpid=os.getgid()

# print(userid)
# print(grpid)

# rename file
# os.rename("/home/vboxuser/python/test/filecreatedbypython.txt", "/home/vboxuser/python/test/REfilecreatedbypython.txt")

# pathvalue=os.path.exists("/etc/hosts")
# print(pathvalue)
# fileexist=os.path.isfile("/etc/hosts")
# print(fileexist)

# filesize=os.path.getsize("/etc/hosts")
# print(filesize)

# joinedpath=os.path.join("/home","pranay")
# print(joinedpath)

# try:
#     open("/etc") # etc is directory not a file , so open() wont work
# except Exception as e:
#     print(e) 

# if os.path.exists("/etc/hosts") and os.path.isfile("/etc/hosts"):
#     print("file exists")
# else:
#     print("file doesnt exist")    




