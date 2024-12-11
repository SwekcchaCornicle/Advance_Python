while True:
    with open('../txt_file/saving_user_data.txt', 'a') as file:
        name = input("Enter name to added: ")
        file.write(name + '\n')
        choice = input("Do you want to add more names? (y/n)")
        if choice == 'n':
            break
with open('../txt_file/saving_user_data.txt', 'r') as file:
    content1 = file.readlines()

for content in content1:
    print(content.strip().capitalize())
