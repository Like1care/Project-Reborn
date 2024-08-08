import logging
import sys
from fastapi import Request




# Get logger
logger = logging.getLogger()

formatter = logging.Formatter(
    
    fmt="	%(asctime)s - %(levelname)s - %(message)s"
)


# Creating hanlers
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')



# Format handlers
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


# Add handlers to logger
logger.handlers = [stream_handler, file_handler]
logger.setLevel(logging.INFO)


# Middleware logger for api application
async def logit(request: Request, call_next):
    
    log_dict = {
        
        'url': request.url.path,
        'method': request.method
    }
    
    logger.info(log_dict, extra=log_dict)
    
    response = await call_next(request)
    
    return response
