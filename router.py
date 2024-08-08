from fastapi import APIRouter
from init import cmc_client

router = APIRouter(prefix="/currencies")

@router.get("")
async def get_cryptocoins():
    
    """Ручка для запроса топ 100 криптовалют с Coinmarketcap."""
    
    return await cmc_client.get_latest()


@router.get("/coin_info/{choice}")
async def get_coin(choice):
    
    """Ручка для вывода полной информации о криптовалюте."""
    
    return await cmc_client.get_coin(choice=choice)


@router.get("/coin_price/{symbol}")
async def get_price(symbol:str):
    
    """Ручка для вывода информации о цене криптовалюты."""
    
    return await cmc_client.get_price(coin_symbol=symbol)