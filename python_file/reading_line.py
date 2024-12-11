# content 1 read is line content 2 read 2nd line
with open('../txt_file/intro.txt', 'r') as file:
    content1 = file.readline()
    content2 = file.readline()
print(content1)

# using this method help to read line in form of list
with open('../txt_file/intro.txt', 'r') as file:
    content1 = file.readlines()
print(content1)

for content in content1:
    print(content)
