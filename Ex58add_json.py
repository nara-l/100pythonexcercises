import json
d = dict(firstName="Albert New", lastName="Bert New")

with open('company1.json', 'r+') as file:
    data = json.loads(file.read())
    data['employees'].append(d)
    file.seek(0)
    json.dump(data, file, sort_keys=True, indent=4)
    file.truncate()
    file.close()
    print("Finished writing to file")

