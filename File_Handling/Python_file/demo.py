# reading file content
file = open('../txt_file/intro.txt', 'r')
content = file.read()
print(content)
file.close()

# can specify number of byte want to read
file = open('../txt_file/intro.txt', 'r')
content = file.read(10)
print(content)
file.close()

# can specify number of byte want to read
file = open('../txt_file/intro.txt', 'r')
content = file.readline()
print(content)
file.close()
