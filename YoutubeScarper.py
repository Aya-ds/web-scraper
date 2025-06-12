import requests
import re
import json

def get_video_info(url):
    try:
        # Get the webpage
        response = requests.get(url)
        response.raise_for_status()
        
        # Extract JSON data from the webpage
        pattern = r'var ytInitialPlayerResponse = ({.*?});'
        match = re.search(pattern, response.text)
        
        if match:
            data = json.loads(match.group(1))
            video_details = data.get('videoDetails', {})
            
            print("Title:", video_details.get('title', 'N/A'))
            print("Views:", video_details.get('viewCount', 'N/A'))
            print("Duration:", video_details.get('lengthSeconds', 'N/A'), "seconds")
            print("Channel:", video_details.get('author', 'N/A'))
            print("Description:", video_details.get('shortDescription', 'N/A')[:200] + "...")
            
        else:
            # Try alternative pattern
            pattern2 = r'"title":"([^"]*)"'
            title_match = re.search(pattern2, response.text)
            if title_match:
                print("Title:", title_match.group(1))
            else:
                print("Could not extract video information")
                
    except Exception as e:
        print(f"Error: {e}")

# Main execution
link = input("Enter the YouTube video link: ")
get_video_info(link)