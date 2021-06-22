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

r = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=0, decode_responses=True)
r.set('mykey', f'Hello from me and you! {stoday}', ex=3600) # ex=expire in Sekunden
value = r.getdel('mykey') #ohne decode wird b' davorgesetzt
print(value, type(value))
