import platform
import os

if platform.system() == 'Linux':
    os.system("ls")
elif platform.system() == 'Windows':
    os.system("dir")
else:
    print("unsupported platform")        


print(platform.python_version())    