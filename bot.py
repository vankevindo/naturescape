import tweepy
import requests
import time
import os

# Replace these with your own API keys
API_KEY = 'your_twitter_api_key'
API_SECRET_KEY = 'your_twitter_secret_key'
ACCESS_TOKEN = 'your_twitter_access_token'
ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'
BEARER_TOKEN = 'your_twitter_bearer_token'
UNSPLASH_ACCESS_KEY = 'your_unsplash_access_key'

def get_random_scenery_image():
    """
    Fetch a random natural scenery image from Unsplash API.
    """
    url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {"query": "nature,scenery,sky,forest,tree,plants,garden,flowers,flower", "orientation": "landscape"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        image_url = data['urls']['regular']  # URL of the image
        image_description = data['description'] or "Beautiful natural scenery"  # Description or fallback
        image_author = data['user']['name']  # Image author
        
        return image_url, image_description, image_author
    else:
        print(f"Failed to fetch image: {response.status_code}")
        return None, None, None

def download_image(image_url):
    """
    Download the image from the URL and save it locally.
    """
    response = requests.get(image_url)
    
    if response.status_code == 200:
        image_path = 'scenery.jpg'
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return image_path
    else:
        print("Failed to download image.")
        return None

def post_tweet_with_image():
    """
    Post a tweet with a random scenery image and description.
    """
    # Create a tweepy Client (API v2) and API (v1.1) instance
    client = tweepy.Client(bearer_token=BEARER_TOKEN,
                           consumer_key=API_KEY,
                           consumer_secret=API_SECRET_KEY,
                           access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_TOKEN_SECRET)

    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Fetch the random scenery image from Unsplash
    image_url, description, author = get_random_scenery_image()

    if image_url:
        # Download the image
        image_path = download_image(image_url)

        if image_path:
            # Tweet content
            tweet_content = f"Photo by {author} on Unsplash"

            try:
                # Upload the media (image) using API v1.1
                media = api.media_upload(image_path)
                
                # Post the tweet with the image using API v2
                client.create_tweet(text=tweet_content, media_ids=[media.media_id])
                print(f"Successfully tweeted with image: {description}")

                # Clean up the downloaded image
                os.remove(image_path)
            except tweepy.TweepyException as e:
                print(f"Failed to post tweet: {e}")
        else:
            print("Image download failed.")
    else:
        print("Failed to get image URL.")

if __name__ == "__main__":
    while True:
        # Post one tweet
        post_tweet_with_image()

        # Wait for 30 minutes (1800 seconds)
        print("Waiting for 30 minutess before posting again...")
        time.sleep(1800)  # 1800 seconds = 30 minutes
