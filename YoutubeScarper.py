from pytube import YouTube
import time

def get_video_info(link):
    try:
        yt = YouTube(link)
        
        # Try to access properties with error handling
        try:
            title = yt.title
        except:
            title = "Could not retrieve title"
            
        try:
            views = yt.views
        except:
            views = "Could not retrieve views"
            
        try:
            length = yt.length
        except:
            length = "Could not retrieve length"
            
        try:
            description = yt.description[:200] + "..." if len(yt.description) > 200 else yt.description
        except:
            description = "Could not retrieve description"
            
        try:
            rating = yt.rating
        except:
            rating = "Could not retrieve rating"
        
        print("Title:", title)
        print("Views:", views)
        print("Duration:", f"{length} seconds" if isinstance(length, int) else length)
        print("Description:", description)
        print("Rating:", rating)
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("This might be due to:")
        print("1. Invalid YouTube URL")
        print("2. Video is private or restricted")
        print("3. pytube needs to be updated")
        print("4. YouTube has changed its API")

# Main execution
link = input("Enter the YouTube video link: ")
get_video_info(link)