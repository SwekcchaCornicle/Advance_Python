with open('../txt_file/intro.txt', 'r') as file:
    content1 = file.readlines()
print(content1)

for content in content1:
    print(content)
for content in content1:
    print(content.strip())
