import os
import re

cover_folder = "./cover/"
name_pattern = re.compile(r"cover(\d+)\.webp")

cnt = 1
for file in os.listdir('./cover'):
    if name_pattern.match(file):
        cnt += 1

current_index = cnt

for file in os.listdir(cover_folder):
    if not name_pattern.match(file):
        new_name = f"cover{current_index}.webp"
        os.rename(os.path.join(cover_folder, file), os.path.join(cover_folder, new_name))
        print(f"{file} -> {new_name}")
        current_index += 1
name_pattern =  re.compile(r'cover(\d+).webp')