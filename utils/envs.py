from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str 
    db_port: int 
    db_name: str 
    db_user: str
    db_password: str
    recipes_appid: str
    recipes_appkey: str
    
    
    class Config:
        env_file = ".env"
        
    
settings = Settings()