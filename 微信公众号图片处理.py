import os
from PIL import Image
from tqdm import tqdm

# Get the list of image files in the current working directory
files = [f for f in os.listdir() if os.path.isfile(f) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

for image_name in tqdm(files):
    # Open the image file
    image = Image.open(image_name)

    # Get the image size
    width, height = image.size

    # Calculate the new size
    if width * height > 600000:
        ratio = (600000 / (width * height)) ** 0.5
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        # Resize the image
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    else:
        # Resize the image
        image = image.resize((width, height), Image.Resampling.LANCZOS)

    # Create the output file name
    base_name, ext = os.path.splitext(image_name)
    output_name = base_name + '_裁剪后' + ext

    # Save the image
    image.save(output_name)

    # Update the progress bar
    tqdm.write(f"{image_name}处理完成")
