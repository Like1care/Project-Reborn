from src_cmc.Client import CMCClient
from src_cmc.config import settings


cmc_client = CMCClient(base_url="https://pro-api.coinmarketcap.com",
                       api_key=settings.CMC_KEY)
