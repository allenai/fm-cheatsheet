import os
import frontmatter
from PIL import Image, ImageDraw, ImageFont

# Define the base directory
base_dir = "content/english/foundation-model-resources/"

# Set debug flag
debug = True

# Iterate over all directories in the base directory
for dir_name in os.listdir(base_dir):
    dir_path = os.path.join(base_dir, dir_name)

    # Check if it's a directory
    if os.path.isdir(dir_path):
        # Iterate over all files in the directory
        for file_name in os.listdir(dir_path):
            # Check if the file is a markdown file
            if file_name.endswith(".md"):
                file_path = os.path.join(dir_path, file_name)

                # Parse the front matter
                with open(file_path, 'r') as file:
                    post = frontmatter.load(file)

                    # Check if 'short_name' is in the front matter
                    if 'short_name' in post.keys():
                        short_name = post['short_name']

                        # Create an image
                        img = Image.new('RGB', (1200, 600), color = (73, 109, 137))

                        d = ImageDraw.Draw(img)
                        # You might need to adjust the font and size
                        fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 55)
                        d.text((100,150), short_name, font=fnt, fill=(255, 255, 0))
                        print("Creating image for " + short_name)
                        # Save the image
                        img.save(os.path.join(dir_path, 'art.png'))

                # If debug flag is set, break after processing one file
                if debug:
                    break

        # If debug flag is set, break after processing one directory
        if debug:
            break
