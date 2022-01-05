import subprocess
import json
import os
import time

#command need to be replaced, see readme
command = ''

#check status every 60 seconds
count = 0
while 1==1:
    return_data = subprocess.check_output(command, shell=True)
    return_data_utf8 = return_data.decode('UTF-8')
    dict_data = json.loads(return_data_utf8)
    response_data = dict_data['responseData']
    for bus in response_data:
        flag = 0
        if bus['checkdedCount'] != 0:
            flag = 1
        if bus['totalPeople'] != bus['maxPeople']:
            flag = 1
        if bus['saleStatus'] != 1:
            flag = 1
        if flag == 1:
            print('*********ticket!!!**********')
            for i in range(0, 100):
                os.system('say "ticket"')
    count += 1
    print(count)
    print(response_data)
    time.sleep(60)
