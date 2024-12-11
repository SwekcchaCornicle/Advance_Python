def save_user_data():
    name = input("Enter Name")
    email = input("Enter email")
    contact = input("enter email")
    user_data = f"Name: {name}\nEmail: {email}\n Contact: {contact}"
    with open("saving_complex.txt", "a") as file:
        file.write(user_data)


save_user_data()
