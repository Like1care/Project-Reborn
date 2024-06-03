from fastapi import FastAPI
from src_cmc.Client import CMCClient
from src_cmc.config import settings


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

@app.get("/cryptocoins?slug={slug}")
async def get_price_info(slug:str):
    
    """Ручка для вывода информации о монете  с помощью query запроса слага (slug) монеты"""
    
    return await cmc_client.get_price_info(slug=slug)

@app.get("/cryptocoins?symbol={sym}")
async def get_price_info(sym:str):
    
    """Ручка для вывода информации о монете с помощью query запроса символа (symbol) монеты"""
    
    return await cmc_client.get_price_info(symbol=sym)
