#coding utf-8
import serial
import re
import requests
import pprint
import json

def main():
    with serial.Serial('COM3',9600,timeout=1) as ser:
        ave = []
        lcnt=0
        while True:
            c = ser.readline()
            d = re.findall('[0-9]+\.+[0-9]',str(c),flags=0)
            d = [float(i) for i in d]
            for i in range(0, len(d)):
                print(d[i])
                ave.append(d[i])
                if lcnt > 10:
                    print('lcnt == 10')
                    if sum(ave)/10 >300:
                        print('over 300!!')
                        print(sum(ave)/10)
                        
                        # Post
                        url = 'http://gomidaru.ap.ngrok.io/garbage/'
                        #json_data = json.dumps({"weight":sum(ave)/10,"id":"abcde","status": "dump"})
                        json_data = json.dumps({"weight":sum(ave)/10,"id":"U76661193c4a0b2f63e9b3364d42ceb7d","status": "dump"})
                        #headers= 'content-type': 'application/json'

                        response = requests.post(url,json_data,headers={'Content-Type': 'application/json'})
                        
                        pprint.pprint(response.json)
                        print(ave)
                    del ave[0:len(ave)]
                    lcnt = 0
            print
            lcnt += 1
        ser.close()

if __name__=="__main__":
    main()