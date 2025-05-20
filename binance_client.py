from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

client = Client(API_KEY, API_SECRET)
client.API_URL = BASE_URL
