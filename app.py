

hosts = r'C:\Windows\System32\drivers\etc\hosts' # r infront of string - passing row string to avoid break lines
direct_to = '127.0.0.1' # localhost
blocked_sites = ['www.linkedin.com', 'linkedin.com']

file = open('C:\Windows\System32\drivers\etc\hosts.txt')

while True:
    print(1)
    