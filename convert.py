import os
from PIL import Image

cover_folder = "./cover/"
output_folder = "./converted_cover/"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(cover_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(cover_folder, filename)
        output_filename = f"{os.path.splitext(filename)[0]}.webp"
        output_path = os.path.join(output_folder, output_filename)
        
        try:
            original_image = Image.open(img_path)
            original_image.save(output_path, 'webp')
            print(f"Converted {filename} to {output_filename}")
        except Exception as e:
            print(f"Error converting {filename}: {str(e)}")