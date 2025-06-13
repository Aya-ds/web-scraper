import instaloader
import os
import requests
from urllib.parse import urlparse

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

def download_profile_picture(profile, folder_name="profile_pics"):
    """
    Download profile picture for a given profile
    """
    try:
        # Create folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Get profile picture URL
        profile_pic_url = profile.profile_pic_url
        
        # Create filename
        filename = f"{profile.username}_profile_pic.jpg"
        filepath = os.path.join(folder_name, filename)
        
        # Download the profile picture
        response = requests.get(profile_pic_url)
        response.raise_for_status()
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Profile picture downloaded: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"✗ Error downloading profile picture for {profile.username}: {str(e)}")
        return None

def download_profile_picture_instaloader(bot, profile, folder_name="profile_pics"):
    """
    Alternative method using instaloader's built-in functionality
    """
    try:
        # Create folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Use instaloader's download_profilepic method
        bot.download_profilepic(profile, target=folder_name)
        print(f"✓ Profile picture downloaded using instaloader for: {profile.username}")
        
    except Exception as e:
        print(f"✗ Error downloading profile picture for {profile.username}: {str(e)}")

# Load a profile from an Instagram handle
print("=== Analyzing Instagram Profile ===")
profile = instaloader.Profile.from_username(bot.context, 'instagram')

print(f"Profile Type: {type(profile)}")
print(f"Username: {profile.username}")
print(f"User ID: {profile.userid}")
print(f"Number of Posts: {profile.mediacount}")
print(f"Followers: {profile.followers}")
print(f"Followees: {profile.followees}")
print(f"External URL: {profile.external_url}")
print(f"Is Private: {profile.is_private}")
print(f"Is Verified: {profile.is_verified}")

# Download profile picture (Method 1 - Manual)
print(f"\n=== Downloading Profile Picture (Method 1) ===")
download_profile_picture(profile)

# Download profile picture (Method 2 - Using instaloader)
print(f"\n=== Downloading Profile Picture (Method 2) ===")
download_profile_picture_instaloader(bot, profile)

print("\n" + "="*50)

# Load a new profile
print("=== Analyzing WWE Profile ===")
profile = instaloader.Profile.from_username(bot.context, 'wwe')

print(f"Username: {profile.username}")
print(f"Followers: {profile.followers}")
print(f"Posts: {profile.mediacount}")

# Download WWE profile picture
print(f"\n=== Downloading WWE Profile Picture ===")
download_profile_picture(profile)

# Get all posts in a generator object
print(f"\n=== Downloading Posts ===")
posts = profile.get_posts()

# Iterate and download (limit to first 5 posts to avoid too many downloads)
max_posts = 5  # Change this number or remove the limit as needed
print(f"Downloading first {max_posts} posts...")

for index, post in enumerate(posts, 1):
    if index > max_posts:
        break
    
    print(f"Downloading post {index}/{max_posts}...")
    try:
        bot.download_post(post, target=f"{profile.username}_{index}")
        print(f"✓ Post {index} downloaded successfully")
    except Exception as e:
        print(f"✗ Error downloading post {index}: {str(e)}")

print(f"\n=== Download Complete ===")
print(f"Check the following folders for downloaded content:")
print(f"- profile_pics/ (for profile pictures)")
print(f"- {profile.username}_1/, {profile.username}_2/, etc. (for posts)")