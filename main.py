from json import load
import redis
import os
from dotenv import load_dotenv

load_dotenv()

HOST = str(os.getenv('HOST'))
PORT = str(os.getenv('PORT'))
PASSWORD = str(os.getenv('PASSWORD'))

r = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=0)
r.set('mykey', 'Hello from me and you!')
value = r.get('mykey') 
print(value)
