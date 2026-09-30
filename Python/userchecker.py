users = {
    "hannah": "user",
    "oliver": "user",
    "camile": "admin",
    "john": "user",
    "emanuel": "admin",
    "anna": "admin",
    "michael": "user",
    "albert": "user",
    "gary": "user",
    "simona": "admin"
}
name = input("Enter your username: ")
if name in users:
        print("Username:", name, "Role:", users[name])
else:
    print("--Username Not Found--")
