import  requests

BASE = 'http://127.0.0.1:5000/'

data = [{"likes": 78, 'name': 'John', 'views': 149}, 
        {"likes": 54, 'name': 'Tim', 'views': 180}, 
        {"likes": 97, 'name': 'Neck', 'views': 200}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + 'video/0')
print(response)

input()
response = requests.get(BASE + 'video/0')
print(response.json())