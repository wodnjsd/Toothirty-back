import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5737/teeth_db')
secret = os.getenv('SECRET', 'Hereisfantasticsecret123')