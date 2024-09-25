from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    
    """Класс - конфигурация"""
    
    CMC_KEY : str
    
    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()