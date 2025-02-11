d = {"name": "Naveen", "age": 25, "city": "Hyderabad", "salary": 50000}

print(d["name"])
d["age"] = 26
print(d)
d["country"] = "India"
print(d)
del d["salary"]
print(d)
popped_value = d.pop("city")
print(d)
print(popped_value)

print(len(d))

keys_sorted = sorted(d.keys())
print(keys_sorted)
