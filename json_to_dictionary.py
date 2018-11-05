import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open('company.json', 'w') as file:

    #json.dump(d, file, indent=4, sort_keys=True)

    file.write(json.dumps(d, indent=4, sort_keys=True))


