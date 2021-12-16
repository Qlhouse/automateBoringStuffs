import os

# Generate ip_list.txt for lan router
with open('ip_list.txt', 'w') as file:
    for i in range(1, 256):
        file.write(f'192.168.1.{i}' + '\n')

# Open ip_list.txt file
with open('ip_list.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    print(dump)

# Print for each ip address
for ip in dump:
    res = os.popen(f'ping {ip}').read()
    if (('无法访问目标主机') or ("请求超时")) in res:
        # print(res)
        f = open('output.txt', 'a')
        f.write(str(ip) + ' is down' + '\n')
        f.close()
    else:
        # print(res)
        f = open('output.txt', 'a')
        f.write(str(ip) + ' is up' + '\n')
        f.close()