import praw
import pandas as pd

reddit = praw.Reddit(
    client_id='XklaFB2839fVxoJ7jrOlIQ',
    client_secret='WyTB6nDQUvrEB0KiDnw-eOTMqzMZcg',
    user_agent='my_bot_v1_pristine123'
)

def scrape_reddit(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.top(limit=10):
        posts.append([post.title, post.author, post.score])
    df = pd.DataFrame(posts, columns=['Title', 'Author', 'Upvotes'])
    df.to_csv(f'{subreddit_name}_top_posts.csv', index=False)
    print(f"Data saved to {subreddit_name}_top_posts.csv")

scrape_reddit('Python')