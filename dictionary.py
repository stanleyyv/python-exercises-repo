# Practicing with dictionary

customer = {
  "name": "Stanley Vuong",
  "age": 29,
  "living": True
}

#replace name with only first name
customer["name"] = "Stanley"
print(customer["name"])
print(customer.get("age"))
#return None
print(customer.get("last name"))

#adding new key and value to dictionary
customer["last name"] = "Vuong"
print(customer.get("last name"))
