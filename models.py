from sqlalchemy import create_engine, Column, Integer, String
from database import Base


class CryptoTweetsList(Base):

    __tablename__ = "crypto_tweets_list"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    symbols = Column(String)
