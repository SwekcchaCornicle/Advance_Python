import json
import os.path


def save_user_data():
    user_list = []
    while True:
        name = input("Enter name (or quit to exit the program):")
        if name == 'quit':
            break
        name = input("Enter Name")
        email = input("Enter email")
        contact = input("enter contact")

        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
        user_list.append(user_data)

    if os.path.exists('../txt_file/serial+deserial.json'):
        with open('../txt_file/serial+deserial.json') as file:
            existing_data = json.load(file)
        user_list.extend(existing_data)

    with open("../txt_file/serial+deserial.json", "w") as file:
        json.dump(user_list, file)

    print("User data save successfully")


save_user_data()
