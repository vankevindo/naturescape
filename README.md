# NatureScape Bot 🌿

**NatureScape Bot** is a Python-based Twitter bot that automatically posts random natural scenery images every 30 minutes using the Unsplash API and Tweepy.

## Features

- Automatically posts a random image of nature every 30 minutes.
- Images are fetched from the Unsplash API based on search queries like "nature, scenery, sky, forest, tree, plants, garden, flowers, flower."
- Posts images to Twitter using Tweepy and includes photo credits in the tweet.

## Technologies Used

- **Python**: The bot is implemented using Python.
- **Requests**: Used to interact with the Unsplash API to fetch random images.
- **Tweepy**: A Python library used to interact with the Twitter API for posting tweets.
- **Unsplash API**: Provides high-quality, royalty-free images from the Unsplash community.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vankevindo/naturescape-bot.git
   cd naturescape-bot
   ```

2. **Install dependencies**:
   Install the required Python packages using `pip`:
   ```bash
   pip install requests tweepy
   ```

3. **Set up API keys**:

   - **Unsplash API**: Sign up for an Unsplash Developer account [here](https://unsplash.com/developers) to get your Access Key.
   - **Twitter API**: Create a Twitter Developer account and set up a new app. You will need the following credentials:
     - API Key
     - API Secret Key
     - Access Token
     - Access Token Secret
     - Bearer Token

4. **Change this line in `bot.py` file** and add your API keys:
   ```bash
   UNSPLASH_ACCESS_KEY=your_unsplash_access_key
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_SECRET_KEY=your_twitter_api_secret_key
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   TWITTER_BEARER_TOKEN=your_bearer_token
   ```

## How to Run

1. **Run the bot**:
   Start the bot by running the following command:
   ```bash
   python bot.py
   ```

2. The bot will post a random natural scenery image every 30 minutes and include the photographer's credit in the tweet. 

## How it Works

1. The bot fetches a random image from the Unsplash API using the following search query:
   ```
   query = "nature,scenery,sky,forest,tree,plants,garden,flowers,flower"
   ```
   This ensures the bot finds images related to nature and landscapes.

2. The bot downloads the image and posts it on Twitter using Tweepy, mentioning the author of the image.

3. After each post, the bot sleeps for 30 minutes (`time.sleep(1800)`) before posting again.

## Customization

- **Search Query**: You can adjust the search query in the `get_random_scenery_image()` function in `bot.py` to fit the type of images you want to post.
- **Posting Interval**: Modify the sleep interval in the `main` function to change how often the bot posts. The current interval is set to 30 minutes (1800 seconds).

## Contributing

Feel free to open an issue or submit a pull request if you have any suggestions or improvements!

## Contact

For any questions or feedback, feel free to reach out on [LinkedIn](https://www.linkedin.com/in/vankevindo/) or [Twitter](https://twitter.com/vankevindo).

---

Enjoy the beauty of nature with every tweet! 🌳🌼
```
