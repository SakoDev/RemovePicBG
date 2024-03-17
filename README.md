## Image Background Removal using Rembg

This Python script allows you to remove backgrounds from images using the Rembg library. It provides a simple command-line interface to process all image files within a specified folder, converting them to PNG format with the background removed. The script utilizes the `rembg` library for background removal and `PIL` (Python Imaging Library) for image manipulation. Progress bars are implemented using `tqdm` to track the processing of each image.

### Features

- Removes backgrounds from images using Rembg library.
- Supports JPEG, PNG, and JPG image formats.
- Converts images to PNG format with the background removed.
- Simple command-line interface.
- Progress bars for tracking image processing.

### Usage

1. Install the required libraries using `pip install -r requirements.txt`.
2. Place your images in a folder named `images`.
3. Run the script. It will process all images in the `images` folder and save the output in a folder named `dist`.

### Requirements
. Python 3.x
. Rembg
. tqdm

```bash
python main.py
```

**Note:** Ensure you have Python installed on your system along with the Rembg library. If Rembg is not already installed, you can install it using pip:

```bash
pip install rembg[gpu,cli]
```

For more information on using *Rembg* and its capabilities, refer to [the Rembg GitHub repository](https://github.com/danielgatis/rembg?tab=readme-ov-file#rembg).

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
