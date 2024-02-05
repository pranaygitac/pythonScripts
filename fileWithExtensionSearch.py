import os 

import argparse

# for dirname, dirpath, filename in os.walk("/etc/ufw/"): # ufw is direct inwhich we r searching
#     #print(dirname,dirpath,filename,"\n")
#     for file in filename:
#         if file == "sysctl.conf": # is name of file we are looking
#             print(os.path.join(dirname,file))

my_parser=argparse.ArgumentParser(description='reading a directory to find file' )
my_parser.add_argument('pathname',
                       help='pls enter dir path')
my_parser.add_argument('filesearch',
                       help='pls enter file name')
args = my_parser.parse_args()

for dirname, dirpath, filename in os.walk(args.pathname): # args.pathname is direct inwhich we r searching
    #print(dirname,dirpath,filename,"\n")
    for file in filename:
        if file == args.filesearch: # rgs.filesearch is name of file we are looking
            print(os.path.join(dirname,file))

# pass "/etc/ufw/" "sysctl.conf" as argument to script    
            
print("#########")     


            
for dirname, dirpath, filename in os.walk(args.pathname):
     # args.pathname is direct inwhich we r searching
    #print(dirname,dirpath,filename,"\n")
    for file in filename:
        if file.endswith('.conf'): # will search for file with .conf extention
            print(os.path.join(dirname,file))



 