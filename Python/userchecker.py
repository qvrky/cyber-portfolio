users = {
    "john": "user",
    "joe": "user",
    "jane": "admin",
    "daniel": "user",
    "anna": "admin",
    "gary": "admin",
    "michael": "user",
    "jason": "user"

}
name = input("Enter your username: ")
if name in users:
        print("Username:", name, "Role:", users[name])
else:
    print("--Username Not Found--")
