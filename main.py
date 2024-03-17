import os
from rembg import remove
from PIL import Image
from glob import glob
from tqdm import tqdm

folder_path = 'images'

image_files = glob(os.path.join(folder_path, "*"))

if not os.path.exists('dist'):
    os.makedirs('dist')

for file in tqdm(image_files, desc="Processing files"):
    file_type = file.split(".")[-1].lower()
    if file_type not in ['jpeg', 'png', 'jpg']:
        print(f"Ignoring file '{file}' as it is not a supported image format.")
        continue

    input_image = Image.open(file)
    output_path = os.path.join('dist', f"{os.path.splitext(os.path.basename(file))[0]}.png")
    output_image = remove(input_image)
    output_image.save(output_path)
