from typing import Optional
from fastapi import FastAPI, Request

# from models import setup_db
from fetch_services import fetch_tweets


def create_app():
    app = FastAPI()
    # setup_db(app)

    @app.get("/")
    async def root():
        return {"message": "hello metaverse"}

    @app.get("/crypto-tweets")
    async def get_tweets_all(symbol: Optional[str]):
        all_tweets = fetch_tweets(symbol)
        return all_tweets

    @app.post("/crypto-tweets-list")
    async def create_crypto_tweets_list(request: Request):
        return await request.json()

    return app


app = create_app()
