# write content in file
# file = open('intro.txt', 'w')
# file.write('New content added to the file')
# file.close()

# append content in file
# file = open('intro.txt', 'a')
# file.write('New content added to the file using append mode')
# file.close()

# append content in file in new line
file = open('../txt_file/intro.txt', 'a')
file.write('\nNew content added to the file using append mode')
file.close()
