import os
import json
from slugify import slugify

# Read the JSON file
with open('/home/iguana/WebstormProjects/fm-cheatsheet/assets/cats.json', 'r') as json_file:
    categories = json.load(json_file)

# Iterate through each category
for category_name, category_data in categories.items():
    # Create directory name from category name
    directory_name = slugify(category_name)
    # Create directory if it doesn't exist
    os.makedirs(directory_name, exist_ok=True)
    # Create index.md file path
    index_file_path = os.path.join(directory_name, 'index.md')
    # Write contents to index.md
    with open(index_file_path, 'w') as index_file:
        index_file.write('---\n')
        index_file.write(f'title: "{category_name}"\n')
        index_file.write(f'short_name: "{category_name}"\n')
        index_file.write('type: "fm-resource-category"\n')
        index_file.write('date: "2024-03-17"\n')  # Update date as needed
        index_file.write(f'description: "{category_data["meta_description"]}"\n') # meta description here
        index_file.write('highlight: true\n')
        index_file.write(f'image: {directory_name}.png\n')  # Update image as needed
        index_file.write(f'details: "{category_data["description"]}"\n') # description here
        index_file.write('---\n')
