import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        'postgresql://postgres.clhjwoarzpcuhrnkdryh:[VODKACOLLECTION125]@aws-0-us-west-1.pooler.supabase.com:6543/postgres'
    )
    
    # Disable modification tracking as it is not needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'default_jwt_secret_key')
