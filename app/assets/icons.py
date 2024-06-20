import os
import requests
import json
from urllib.parse import urlparse

def get_github_profile_logo(github_link, save_dir, github_token):
    if github_link == "":
        return None

    # Extracting username and repository from GitHub link
    parsed_url = urlparse(github_link)
    path_parts = parsed_url.path.strip("/").split("/")
    if len(path_parts) < 1:
        print(f"Invalid GitHub link: {github_link}")
        return None
    username = path_parts[0]

    # Making a request to GitHub API to get user information
    api_url = f"https://api.github.com/users/{username}"
    headers = {
        'Authorization': f'token {github_token}',
        'User-Agent': 'Your-User-Agent'  # Replace 'Your-User-Agent' with your actual user agent
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        profile_logo_url = user_info['avatar_url']

        # Downloading the profile logo and saving it to the specified directory
        logo_filename = f"{username}_logo.png"
        logo_filepath = os.path.join(save_dir, logo_filename)
        with open(logo_filepath, 'wb') as f:
            f.write(requests.get(profile_logo_url).content)

        return logo_filepath
    else:
        print(f"Failed to fetch profile logo for {github_link}")
        print(f"GitHub API response: {response.status_code} - {response.reason}")
        return None


def update_resources_json(resources, github_profile_logos, resources_file):
    for i, resource in enumerate(resources):
        if i < len(github_profile_logos):  # Check index to avoid out of bounds
            logo_path = github_profile_logos[i]
            resource['logo'] = os.path.basename(logo_path)
        else:
            resource['logo'] = ""  # Or provide a default placeholder

    with open(resources_file, 'w') as f:
        json.dump(resources, f, indent=2)

def main():
    resources_file = '/home/iguana/WebstormProjects/fm-cheatsheet/assets/resources.json'
    save_dir = '/home/iguana/WebstormProjects/fm-cheatsheet/assets/images/gh-icons'
    github_token = ''  # Replace 'Your-GitHub-Token' with your actual GitHub token

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    with open(resources_file) as f:
        resources = json.load(f)

    for resource in resources:
        github_link = resource.get('github_link')
        if github_link:  # Only process resources with a GitHub link
            profile_logo_path = get_github_profile_logo(github_link, save_dir, github_token)
            if profile_logo_path:
                resource['logo'] = os.path.basename(profile_logo_path)
                # Update resources.json immediately
                with open(resources_file, 'w') as f:
                    json.dump(resources, f, indent=2)

    print("GitHub profile logos saved to:", save_dir)  # All logos saved
    print("resources.json updated with logo property")  # resources.json is already updated

if __name__ == "__main__":
    main()
