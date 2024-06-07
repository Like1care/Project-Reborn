from loguru import logger


logger.remove()

logger.add(
    "logs.json",
    format="{time:MMMM D, YYYY - HH:mm:ss} {level} --- {message}",
    level="DEBUG",
    serialize=True,
    rotation="10 MB"
)

def get_log(func_name:str, req_name:str, cryptocurrency:str):
    
    logger.debug(f"Request: {req_name} Cryptocurrency: {cryptocurrency} ---{func_name}---")
    