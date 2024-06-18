from aiohttp import ClientSession
#Query запросы работают некорректно !!!!

class HttpClient:
    
    def __init__(self, base_url:str, api_key:str):
        
        self._session = ClientSession(base_url=base_url, headers={
            "X-CMC_PRO_API_KEY" : api_key,
            })

class CMCClient(HttpClient):
    
    async def get_latest(self):
        
        """Функция вывода топ 100 монет с Coinmarketcap"""
        
        async with self._session.get('/v1/cryptocurrency/listings/latest') as resp:
            
            result = await resp.json()
            
            return result["data"]
    
    async def get_coin(self, coin_id:int):
        
        """Выод информации о монете по ID"""
        
        async with self._session.get('/v2/cryptocurrency/quotes/latest', params={"id":coin_id}) as resp:
            
            result = await resp.json()
            
            return result["data"][str(coin_id)]
    
    
    async def get_price_info(self, coin_slug=None, coin_symbol=None):
        
        """Вывод информации о монете по слагу(имени) или символу монеты."""
        
        try:
            if coin_slug:
                async with self._session.get('/v2/cryptocurrency/quotes/latest?slug', params={"slug": coin_slug}) as resp:
                    
                    result = await resp.json()
                    key = ''.join(result.keys())
                    return result[key]['data']
            else:
                async with self._session.get('/v2/cryptocurrency/quotes/latest?symbol', params={"symbol": coin_symbol}) as resp:
                    
                    result = await resp.json()
                    key = ''.join(result.keys())
                    return result[key]['data']
        except:
            return None
