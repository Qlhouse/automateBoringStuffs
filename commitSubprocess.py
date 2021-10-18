import subprocess

videoURL = ''

'''
while True:
    p1 = subprocess.run(f'you-get {videoURL}', shell=True)
    if p1.returncode == 0:
        break
'''

subprocess.call('dir', shell=True)