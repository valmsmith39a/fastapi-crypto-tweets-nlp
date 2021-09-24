from typing import Optional
from fastapi import FastAPI
from fetch_services import fetch_tweets

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello metaverse"}

@app.get("/crypto-tweets")
async def get_tweets_all(symbol: Optional[str]):
    all_tweets = fetch_tweets(symbol)
    return all_tweets
