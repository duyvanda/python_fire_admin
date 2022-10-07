import json

# json_data = json.dumps()

with open('PhuongXa.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

for index, el in enumerate(data):
    if index == 10700:
        print(el)
        break

# for index, el in enumerate(data):
#     print(index)