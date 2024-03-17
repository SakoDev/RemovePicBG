from rembg import remove
from PIL import Image
from glob import glob
from tqdm import tqdm

file_type = input("Enter the file type you want to process (jpeg/png/jpg): ").lower()

if file_type not in ['jpeg', 'png', 'jpg']:
    print("Invalid file type. Please enter either 'jpeg', 'png', or 'jpg'.")
    exit()

if file_type == 'jpeg':
    files = glob("img_jpeg/*.jpeg")
elif file_type == 'png':
    files = glob("img_png/*.png")
else:  
    files = glob("img_jpg/*.jpg")

for file in tqdm(files, desc="Processing Remove Background"):
    input_path = file
    output_path = file.replace("img_" + file_type, "dist")
    output_path = output_path.replace(file_type, "png")
    input_image = Image.open(input_path)
    output_image = remove(input_image, alpha_matting=True, alpha_matting_foreground_threshold=270,alpha_matting_background_threshold=20, alpha_matting_erode_size=11)
    output_image.save(output_path)
