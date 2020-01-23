import time
from datetime import datetime as dt

hosts = r'C:\Windows\System32\drivers\etc\hosts' # r infront of string - passing row string to avoid break lines
direct_to = '127.0.0.1'
blocked = ['www.linkedin.com', 'linkedin.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 7) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 15):
        print('Working...')
        with open(hosts, 'r+') as file:
            content = file.read()
            for b in blocked: # check blocked list
                if b in content: 
                    pass # if in blocked list continue
                else:
                    file.write(direct_to + ' ' + b + '\n')
    else:
        with open(hosts,'r+') as file:
            content = file.readlines()
            file.seek(0) # Move curser to top of file
            for line in content:
                if not any(b in line for b in blocked):
                    file.write(line)
            file.truncate() # Remove anything below new write
            print('Browse away..')

    time.sleep(5) # script executes every 5 seconds for testing / change to 300 on completion