from fastapi import FastAPI
from src.Client import CMCClient
from src.config import settings


app = FastAPI()

cmc_client = CMCClient(base_url="https://pro-api.coinmarketcap.com", api_key=settings.CMC_KEY)

@app.get("/cryptocoins")
async def get_cryptocoins():
    
    return await cmc_client.get_latest()


@app.get("/cryptocoins/{coin_id}")
async def get_coin(coin_id:int):
    
    return await cmc_client.get_coin(coin_id=coin_id)