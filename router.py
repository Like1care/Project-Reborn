from fastapi import APIRouter
from init import cmc_client

router = APIRouter(prefix="/currencies")

@router.get("")
async def get_cryptocoins():
    
    """Ручка для запроса топ 100 монет с Coinmarketcap"""
    
    return await cmc_client.get_latest()


@router.get("/cryptocoins/{coin_id}")
async def get_coin(coin_id:int):
    
    """Ручка для вывода информации о монете через ID монеты"""
    
    return await cmc_client.get_coin(coin_id=coin_id)


@router.get("/coin_info/{symbol}")
async def get_price(symbol:str):
    
    return await cmc_client.get_price(coin_symbol=symbol)