from fastapi import FastAPI
from src_cmc.Client import CMCClient
from src_cmc.config import settings
from logs.logger import get_log


#Query запросы работают некорректно !!!!


app = FastAPI()

cmc_client = CMCClient(base_url="https://pro-api.coinmarketcap.com", api_key=settings.CMC_KEY)

@app.get("/cryptocoins")
async def get_cryptocoins():
    
    """Ручка для запроса топ 100 монет с Coinmarketcap"""
    
    return await cmc_client.get_latest()


@app.get("/cryptocoins/{coin_id}")
async def get_coin(coin_id:int):
    
    """Ручка для вывода информации о монете через ID монеты"""
    
    return await cmc_client.get_coin(coin_id=coin_id)


@app.get("/coin_info/{symbol}")
async def get_price(symbol:str):
    
    return await cmc_client.get_price(coin_symbol=symbol)

