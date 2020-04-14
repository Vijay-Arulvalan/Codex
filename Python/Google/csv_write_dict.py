users = [{"name": "chris", "username": "chrisy", "department": "IT infrastructure"},{"name": "lional", "username": "lio", "department": "user experiment reserach"}, {"name": "charlie", "username": "grayc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.Dictwriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
