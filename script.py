# this script is used to generate the file list for random picture 
import os

dir = './cover'
pic_prefix = 'http://fastly.jsdelivr.net/gh/jenway/J-figure-bed@master/cover/'

def get_file_list(dir):
    file_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                file = pic_prefix + file
                file_list.append(file)
                print("file: " + file + " added")
    return file_list

# save file_list as img.txt

file_list = get_file_list(dir)
with open('img.txt', 'w') as f:
    for file in file_list:
        f.write(file + '\n')

print("file list generated")
