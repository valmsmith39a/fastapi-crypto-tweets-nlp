from fastapi import FastAPI
from fetch_services import fetch_tweets

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello metaverse"}

@app.get("/tweets/all")
async def get_tweets_all():
    all_tweets = fetch_tweets()
    return all_tweets
