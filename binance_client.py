from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

# Criação do client para Testnet de forma correta
client = Client(API_KEY, API_SECRET, testnet=True)
# Não altere client.API_URL manualmente
