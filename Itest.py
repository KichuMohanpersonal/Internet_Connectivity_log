#!/usr/bin/python3

import urllib 
from urllib.request import urlopen
import time


    


print("Internet Test logger")
print("\n")
limit = int(input("Enter limit in Min: "))
flag = 1
count =0

limit = limit*60
inc = 5

F = open("Log_Asianet.txt","w")
F.write("Internet Test logger               -client = Asianet\n\n\n\n")




for i in range(0,limit,inc):
    
    try: 
        
        s = urlopen('https://google.com/',timeout=1)
        if(flag == 0):
            sec = time.time()
            local_time = time.ctime(sec)
            F.write("Internet available ------Time: ")
            F.write(str(local_time))
            F.write("\n")
            print("Internet available---",end = '')
            print("--Time:", local_time)	
            
            flag = 1
    except:
        if(flag == 1):
            seconds = time.time()
            local_time = time.ctime(seconds)
            
            F.write("No internet connection------Time: ")
            F.write(str(local_time))
            F.write("\n")
            print("No internet connection---",end='')
            print("---Time:", local_time)
            count = count + 1	
            
            flag = 0
    
    time.sleep(inc)
F.write("\n\n\n              Network Disconnect Frequency :  ")
F.write(str(count))
   
F.close()
