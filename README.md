**Background Removal Script with Rembg**

This Python script is designed to streamline the process of removing backgrounds from images using the Rembg library. By running this script, users can effortlessly process a batch of images, selecting the desired file type (JPEG, PNG, or JPG) for background removal.

**Instructions:**

1. **Choose File Type:** When prompted, enter the file type of the images you want to process. You can choose from JPEG, PNG, or JPG. Simply type the corresponding file extension (e.g., "jpeg", "png", or "jpg") when prompted.

2. **Process Images:** Once you've specified the file type, the script automatically locates the corresponding directory containing images of the selected type. It then proceeds to process each image within the directory, removing its background.

3. **Monitor Progress:** Throughout the processing, a progress bar is displayed, providing real-time feedback on the completion status of background removal for each image.

4. **View Output:** The processed images are saved in a designated output directory named "dist". You can find the background-free versions of your images in this directory, saved in the PNG format.

**Example Usage:**

Suppose you have a directory named "img_jpg" containing JPEG images that you want to process. Running this script will prompt you to enter the file type ("jpeg", "png", or "jpg"). After selecting "jpeg", the script will process each JPEG image in the "img_jpg" directory, removing its background and saving the resulting images in the "dist" directory.

**Note:** Ensure you have Python installed on your system along with the Rembg library. If Rembg is not already installed, you can install it using pip:

```bash
pip install rembg[gpu,cli]
```

For more information on using *Rembg* and its capabilities, refer to the Rembg GitHub repository.
