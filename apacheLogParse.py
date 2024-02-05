import re 
from collections import Counter
import csv
#import argparse
logfile="apache_logs"
logreg="[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"

with open(logfile) as f:
    log = f.read()
    ip_list = re.findall(logreg, log)
    #print(ip_list)
    #print(Counter(ip_list))
    # for k,v in Counter(ip_list).items():
    #     print(k,v)
    with open("ipcount.csv","w") as f:
        fwritecsv=csv.writer(f)
        fwritecsv.writerow(["ip_addr","count"])
        for k,v in Counter(ip_list).items():
            fwritecsv.writerow([k,v])
   