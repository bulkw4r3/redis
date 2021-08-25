import redis
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
PASSWORD = os.getenv('PASSWORD')

today = datetime.datetime.now()
stoday = today.isoformat() #convert date to string

r = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=1, decode_responses=True)
#r.set('mykey', f'Hello from me and you! Timestamp: {stoday}', ex=3600) # ex=expire in Sekunden
r.sadd('testkey', '7', '6', '8', '9', '11')
#value = r.get('mykey') #ohne decode wird b' davorgesetzt
value = r.smembers('testkey')
print(value)
