#JSON DATASI

import json

data = '{"firstName":"Bukish","LastName":"Pussy Destroyer"}'

y = json.loads(data)
print(y["firstName"])
print(y["LastName"])

customer = {
    "firstName":"Buko",
    "Mail":"buketozceylan@outlook.com"
    }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Bukiiii"))
