#! /usr/bin/python
import socket
import time
import requests



###############################################################################
#
# Check URls - IP Telecom | Version 0.1 
# @Pedro M and @Jose G.
#
###############################################################################


#li = open('/Users/pedromagalhaes/Desktop/lista.txt').readlines()

#remove \n problem with list
with open('/Users/pedromagalhaes/Desktop/lista.txt', 'r') as f:
    lines = f.readlines()
    
final_list = []
for i in lines:

 final_list.append("https://"+i.strip()+"/")

print(final_list)

teste=1

###############################################################################
# MAP Colour and Core Functions
###############################################################################
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
def main():
    #while teste==True:
        print ("\nTesting URLS.", time.ctime())
        checkUrls()
        print ("Press CTRL+C to exit")
        time.sleep(10) #Sleep 10 seconds
        teste=0
def checkUrls():
    for url in final_list:
        status = "N/A"
        try:
            status = checkUrl(url)
        except requests.exceptions.ConnectionError:
            status = "DOWN"
            print(requests.exceptions.ConnectionError())

        printStatus(url, status)

def checkUrl(url):

     r = requests.head(url,allow_redirects=True, timeout=6)
    #print r.status_code
     return str(r.status_code)

def printStatus(url, status):

    color = GREEN

    if status >= "404":
        color=RED

    if status == "403":
        color=YELLOW
        f = open("/Users/pedromagalhaes/Desktop/resultadosURLS.txt", "a")
        f.write(url+"\n")
        f.close()    

    if status == "200":
      
      f = open("/Users/pedromagalhaes/Desktop/resultadosURLS.txt", "a")
      f.write(url+"\n")
      f.close()

    print (color+status+ENDC+' '+ url)

#
# MAIN START
#
if __name__ == '__main__':
    if (teste == 1):
     main()
else:
    exit()